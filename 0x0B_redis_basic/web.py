#!/usr/bin/env python3
"""
Web cache with Redis
"""

import redis
import requests
from functools import wraps

redis_client = redis.Redis()


def get_page(url: str) -> str:
    """
    Fetch HTML content of a URL with caching and access count.
    """

    count_key = f"count:{url}"

    # increment access counter
    redis_client.incr(count_key)

    # check cache first
    cached_page = redis_client.get(url)
    if cached_page:
        return cached_page.decode("utf-8")

    # fetch from web if not cached
    response = requests.get(url)
    html = response.text

    # store in cache with 10 second expiration
    redis_client.setex(url, 10, html)

    return html
