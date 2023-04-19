#!/usr/bin/env python3
"""MRU caching algorithm module"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU Caching algorithm class"""
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        """Add item to cache using mru strategy"""
        if key is not None or item is not None:
            if key in self.cache_data.keys():
                self.cache_data.pop(key)
            data = {
                key: item
            }
            self.cache_data = {**data, **self.cache_data}

            if len(self.cache_data) > self.MAX_ITEMS:
                recentItem = list(self.cache_data.keys())[1]
                self.cache_data.pop(recentItem)
                print(f'DISCARD: {recentItem}')

    def get(self, key):
        """Get item from cache with mru strategy"""
        if key is None or key not in self.cache_data:
            return None
        if key in self.cache_data.keys():
            item = self.cache_data[key]
            self.cache_data.pop(key)
            data = {
                key: item
            }
            self.cache_data = {**data, **self.cache_data}
        return self.cache_data[key]
