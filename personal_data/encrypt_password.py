#!/usr/bin/env python3
"""Module to hash passwords securely using bcrypt"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt.

    Args:
        password (str): The password in unhashed

    Returns:
        bytes: The salted, hashed password
    """
    salty = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salty)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Comparing hashed password against password

    Args:
        hashed password in bytes and the password in str

    Return:
        Boolean value, true if the password matches, false otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
