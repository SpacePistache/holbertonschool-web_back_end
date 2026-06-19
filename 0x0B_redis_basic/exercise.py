#!/usr/bin/env python3
"""A module that writes a string to Redis and then flushes it"""


import redis
import uuid
from typing import Union, Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """history of function calls"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))

        output = method(self, *args, **kwargs)

        self._redis.rpush(output_key, str(output))

        return output

    return wrapper

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

    @call_history
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

    def get_str(self, key: str) -> str:
        """retrieve string value"""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """retrieve int value"""
        return self.get(key, int)
