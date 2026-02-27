#!/usr/bin/env python3
"""A module that imports from auth.py to create a basic authentication"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic auth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Return Base64 auth header"""

        if authorization_header is None:
            return None

        if not isinstance(self.authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split("Basic ")[1]
