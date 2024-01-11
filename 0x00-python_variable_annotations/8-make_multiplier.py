#!/usr/bin/env python3
""" Complex types - functions """
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """ Return a function """
    def f(n: float) -> float:
        """ Return the multiplication of a float with multiplier """
        return n * multiplier
    return f
