#!/usr/bin/env python3
"""A module that writes a string to Redis and then flushes it"""


import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count calls"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)

        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """Cache class for storing data in Redis"""

    def __init__(self):
        """stores instance of private variable then flushes it."""
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generates a random key and stores input data"""
        key = str(uuid.uuid4())

        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Callable = None):
        """Retrieve data from Redis"""
        value = self._redis.get(key)

        if value is None:
            return None

        if fn is None:
            return value

        return fn(value)

    def get_str(self, key: str) -> int:
        """retrieve string value"""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """retrieve int value"""
        return self.get(key, int)
