#!/usr/bin/env python3
"""A module generating a random int and waiting between each iteration"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Coroutine that loops 10x"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
