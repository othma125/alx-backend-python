#!/usr/bin/env python3
""" Async Generator """
import asyncio
from random import uniform


async def async_generator():
    """ Async Generator """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)