#!/usr/bin/env python3
"""A module that collects 10 random numbers using an async
comprehensing over async_generator,
then return the 10 random numbers.
"""
import asyncio
import random
from typing import AsyncGenerator
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def async_comprehension() -> AsyncGenerator[float, None]:
    for _ in range(10):
        yield random.randint(0, 10)
        asyncio.sleep(1)
