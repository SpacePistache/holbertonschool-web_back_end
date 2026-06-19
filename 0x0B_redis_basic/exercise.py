#!/usr/bin/env python3
"""A module that writes a string to Redis and then flushes it"""


import redis
import uuid
from typing import Union


class Cache:
    """Cache class for storing data in Redis"""

    def __init__(self):
        """stores instance of private variable then flushes it."""
        #self._redis = redis.Redis()
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generates a random key and stores input data"""
        key = str(uuid.uuid4())

        self._redis.set(key, data)

        return key
