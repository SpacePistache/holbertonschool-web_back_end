#!/usr/bin/env python3
"""A module that imports from auth.py to create a basic authentication"""

from api.v1.auth.auth import Auth
from models.user import User
import base64


class BasicAuth(Auth):
    """Basic auth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Return Base64 auth header"""

        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Return decoded string"""
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """Return user email and password from decoded Base64 value"""

        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        user_email, user_pwd = \
            decoded_base64_authorization_header.split(':', 1)

        return user_email, user_pwd

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str):
        """Return User instance based on email and password"""

        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        if not users:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None):
        """Retrieve User instance for a request"""

        authorization_header = self.authorization_header(request)

        base64_header = self.extract_base64_authorization_header(
            authorization_header
        )

        decoded_header = self.decode_base64_authorization_header(
            base64_header
        )

        user_email, user_pwd = self.extract_user_credentials(
            decoded_header
        )

        return self.user_object_from_credentials(
            user_email,
            user_pwd
        )
