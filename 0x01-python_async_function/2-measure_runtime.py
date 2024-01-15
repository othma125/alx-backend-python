#!/usr/bin/env python3
"""measure_time module
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_runtime(n: int, max_delay: int) -> float:
    """

    Returns:
        float: [description]
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time/n
