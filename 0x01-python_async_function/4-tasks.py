#!/usr/bin/env python3
"""task_wait_n module
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times"""
    delays = []
    for task in \
            asyncio.as_completed([task_wait_random(max_delay) for _ in range(n)]):
        delays.append(await task)
    return delays
