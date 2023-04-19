#!/usr/bin/env python3
"""LIFO caching algorithm module"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        """Add item to cache"""
        if key is not None or item is not None:
            if key in self.cache_data.keys():
                self.cache_data.pop(key)
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                lastItemBeforeInsert = list(self.cache_data.keys())[-2]
                self.cache_data.pop(lastItemBeforeInsert)
                print(f'DISCARD: {lastItemBeforeInsert}')

    def get(self, key):
        """Get item from cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
