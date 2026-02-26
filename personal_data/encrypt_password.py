#!/usr/bin/python3

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
