#!/usr/bin/env python3
""" Session authentication views """
from api.v1.views import app_views
from flask import request, jsonify, make_response
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """login route for session auth"""

    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400

    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    response = jsonify(user.to_json())
    session_name = getenv("SESSION_NAME")
    response.set_cookie(session_name, session_id)

    return response
