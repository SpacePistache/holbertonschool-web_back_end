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
        return False


    def authorization_header(self, request=None) -> str:
        """None for now"""
        return None


    def current_user(self, request=None) -> User:
        """None for now"""
        return None
