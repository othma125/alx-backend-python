#!/usr/bin/env python3
"""[summary]
"""
from asyncio import sleep
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """[summary]

    Args:
        max_delay (int, optional): [description]. Defaults to 10.

    Returns:
        float: [description]
    """
    random_delay: float = uniform(0, max_delay)
    await sleep(random_delay)
    return random_delay
