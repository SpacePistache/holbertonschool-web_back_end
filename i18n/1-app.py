#!/usr/bin/env python3
"""Basic flask app with babel config"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
Babel = __import__ ('1-app').babel


@app.route('/')
def home():
    """home route"""

    return render_template('0-index.html')


if __name__ == '__main__':
    app.run
