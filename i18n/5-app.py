#!/usr/bin/env python3
"""Flask app with mock login system"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


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
    """Retrieve user based on login_as param"""
    user_id = request.args.get('login_as')

    if user_id:
        try:
            return users.get(int(user_id))
        except (ValueError, TypeError):
            return None
    return None


@app.before_request
def before_request():
    """Set user in global request context"""
    g.user = get_user()

def get_locale():
    """Determine best locale"""

    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.get('user') and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """Home route"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
