#!/usr/bin/env python3
"""
This module defines an async routine concurrently waiting for
multiple random delays and returns a list of completed delay times
chronologically
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and
    returns the list of all delays in the order they complete.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        List[float]: List of delays in the order they completed.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        delays.append(result)

    return delays
