#!/usr/bin/env python3
"""
hypermedia pagination module
"""


import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index range"""
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
        result: Tuple[int, int] = index_range(page, page_size)
        dataset: List[List] = self.dataset()
        return dataset[result[0]: result[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> \
            Dict[str, int | None]:
        """get hypermedia metadata for specified page and page size"""
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(dataset) / page_size)

        if self.get_page(page+1, page_size) == []:
            next_page = None
        else:
            next_page = page + 1

        if page == 1:
            prev_page = None
        elif page > 1:
            prev_page = page - 1
        diction = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            'prev_page': prev_page,
            "total_pages": total_pages
        }
        return diction
