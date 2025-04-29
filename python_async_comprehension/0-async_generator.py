#!/usr/bin/env python3
"""A module generating a random int and waiting between each iteration"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Coroutine that loops 10x"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
