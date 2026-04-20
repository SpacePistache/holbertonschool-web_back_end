#!/usr/bin/env python3
"""Method that takes password
string and returns bytes"""

import bcrypt


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
