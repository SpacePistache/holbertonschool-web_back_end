#!/usr/bin/env python3
"""A module that writes a string to Redis and then flushes it"""


import redis
import uuid


class Cache:

    def __init__(self):
        self._redis = redis.Redis()
        self._redis = flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        key = str(uuid(4))

        self._redis.set(key, data)

        return key
