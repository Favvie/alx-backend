#!/usr/bin/env python3
"""simple helper function module"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of start index and end index"""
    start_index: int = (page * page_size) - page_size
    end_index: int = page_size * page
    result: tuple(int, int) = (start_index, end_index)
    return result
