#!/usr/bin/env python3
"""simple pagination"""
import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert page > 0
        assert page_size > 0
        index_tuple = index_range(page, page_size)
        self.dataset()
        return self.__dataset[index_tuple[0]:index_tuple[1]]
