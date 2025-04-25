#!/usr/bin/env python3
"""
Module defining a coroutine generating multiple wait_random tasks
using a helper function, and returns a list of results in completion order.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with specified max_delay and returns
    list of all delays in the order they are completed.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of delays in the order the tasks completed.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for completed in asyncio.as_completed(tasks):
        result = await completed
        delays.append(result)

    return delays
