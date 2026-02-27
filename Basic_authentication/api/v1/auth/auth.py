#!/usr/bin/env python3
"""Authentication module"""

from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth():
    """Authentication blueprint"""

    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """False for now"""

        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """None for now"""
        return None

    def current_user(self, request=None) -> User:
        """None for now"""
        return None
