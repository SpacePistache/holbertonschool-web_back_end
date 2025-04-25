#!/usr/bin/env python3
import asyncio
import random
"""Module is an asynchronous coroutine waiting for a random delay"""


async def wait_random(max_delay: int = 10) -> float:
    """
        Args:
        max_delay (int): The maximum number of seconds to wait. Default is 10.

    Returns:
        float: The random delay that was waited before returning.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
