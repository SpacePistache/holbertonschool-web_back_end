#!/usr/bin/env python3
"""
Module defining a function to measure the average execution time
of an asynchronous coroutine running multiple delay tasks concurrently.
"""

import time
import asyncio
from typing import Callable
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time of wait_n and returns average delay time.

    Args:
        n (int): Number of times wait_n will spawn coroutines.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: Average time taken per coroutine.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()

    total_time = end - start
    return total_time / n
