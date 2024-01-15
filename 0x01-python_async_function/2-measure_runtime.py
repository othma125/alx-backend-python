#!/usr/bin/env python3
"""measure_time module
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_runtime(n: int, max_delay: int = 10) -> float:
    """

    Returns:
        float: [description]
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
