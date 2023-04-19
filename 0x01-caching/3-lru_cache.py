#!/usr/bin/env python3
"""LRU caching algorithm module"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching algorithm class"""
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        """Add item to cache using lru strategy"""
        if key is not None or item is not None:
            if key in self.cache_data.keys():
                self.cache_data.pop(key)
            data = {
                key: item
            }
            self.cache_data = {**data, **self.cache_data}

            if len(self.cache_data) > self.MAX_ITEMS:
                lastItemBeforeInsert = list(self.cache_data.keys())[-1]
                self.cache_data.pop(lastItemBeforeInsert)
                print(f'DISCARD: {lastItemBeforeInsert}')

    def get(self, key):
        """Get item from cache with lru strategy"""
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
