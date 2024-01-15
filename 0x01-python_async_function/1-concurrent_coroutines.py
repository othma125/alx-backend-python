#!/usr/bin/env python3
"""wait_n module
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """[summary]

    Args:
        n (int, optional): [description]. Defaults to 0.
        max_delay (int, optional): [description]. Defaults to 10.

    Returns:
        list[float]: [description]
    """
    delays = []
    for task in \
            asyncio.as_completed([wait_random(max_delay) for _ in range(n)]):
        delays.append(await task)
    return delays
