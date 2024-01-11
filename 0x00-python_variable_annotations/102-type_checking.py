#!/usr/bin/env python3
""" Basic annotations - to string """
from typing import Union, List, Tuple, Callable, Iterator


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Return a list """
    zoomed_in: Callable[[Tuple, int], Iterator[Union[int, str]]] = \
        lambda lst, factor=2: (
            item for item in lst for i in range(factor)
        )
    return list(zoomed_in(lst, factor))
