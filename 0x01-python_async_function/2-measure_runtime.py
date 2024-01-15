#!/usr/bin/env python3
"""measure_time module
"""
import asyncio
measure_time = __import__('2-measure_runtime').measure_time


def measure_runtime() -> float:
    """

    Returns:
        float: [description]
    """
    start_time = asyncio.get_event_loop().time()
    asyncio.run(measure_time())
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
