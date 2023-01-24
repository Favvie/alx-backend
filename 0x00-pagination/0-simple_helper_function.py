#!/usr/bin/env python3
"""simple helper function"""


def index_range(page, page_size):
    """
    a function that takes a page number and page size and returns
    a tuple of a start index and an end index
    """
    start_index = 0
    if page == 0:
        start_index = 1
        value = start_index * page_size
    else:
        value = page * page_size
        for i in range(page - 1):
            start_index = start_index + page_size
    return (start_index, value)
