#!/usr/bin/env python3
"""
simple pagination module
"""


import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of start index and end index"""
    start_index: int = (page * page_size) - page_size
    end_index: int = page_size * page
    result: tuple(int, int) = (start_index, end_index)
    return result


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
        """get data for a page from dataset based on page size"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        result = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[result[0]: result[1]]
