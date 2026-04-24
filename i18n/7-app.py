#!/usr/bin/env python3
"""Flask app with timezone support"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


class Config:
    """Config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()


def get_user():
    """Retrieve user from login_as param"""
    user_id = request.args.get('login_as')

    if user_id:
        try:
            return users.get(int(user_id))
        except (ValueError, TypeError):
            return None
    return None


@app.before_request
def before_request():
    """Set user globally"""
    g.user = get_user()


def get_locale():
    """Determine best locale"""

    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.get('user'):
        user_locale = g.user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone():
    """Determine best timezone"""

    tz = request.args.get('timezone')
    if tz:
        try:
            return pytz.timezone(tz).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.get('user'):
        user_tz = g.user.get('timezone')
        if user_tz:
            try:
                return pytz.timezone(user_tz).zone
            except pytz.exceptions.UnknownTimeZoneError:
                pass

    # 3. Default
    return "UTC"


babel.init_app(
    app,
    locale_selector=get_locale,
    timezone_selector=get_timezone
)


@app.route('/')
def index():
    """Home route"""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()
