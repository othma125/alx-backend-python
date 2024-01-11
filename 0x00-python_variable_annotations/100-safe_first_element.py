#!/usr/bin/env python3
""" Basic annotations - safe first element of a sequence """
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Return the first element of a list """
    if lst:
        return lst[0]
    return None
