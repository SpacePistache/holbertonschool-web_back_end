#!/usr/bin/env python3
""" Session authentication module """
from api.v1.auth.auth import Auth
from models.user import User
import uuid
from os import getenv
from flask import request, jsonify
from api.v1.views import app_views


class SessionAuth(Auth):
    """ SessionAuth class """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create session for id"""
        if user_id is None or type(user_id) is not str:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """create user id fpr sesion"""
        if session_id is None or type(session_id) is not str:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Returns a User instance based on a cookie """

        if request is None:
            return None

        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        return User.get(user_id)


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """login route for sesh auth"""

    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == "":
        return jsonify({"error: email missing"}), 404

    if password is None or password == "":
        return jsonify({"error: wrong password"}), 401

    users = User.search({'email': email})
    if not users:
        return jsonify({"error: no user found with this email."}), 404

    user = users[0]

    from api.v1.app import auth

    session_id = auth.create_session(user.id)

    response = jsonify(user.to_json())

    session_name = getenv("SESSION_NAME")
    response.set_cookie(session_name, session_id)

    return response
