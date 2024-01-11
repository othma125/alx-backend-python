#!/usr/bin/env python3
""" Basic annotations - safe first element of a sequence """
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Return the first element of a list """
    if key in dct:
        return dct[key]
    return default
