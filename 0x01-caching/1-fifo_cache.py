#!/usr/bin/env python3
"""Fifo caching algorithm module"""
BaseCache = __import__('base_caching').BaseCaching


class FIFOCache(BaseCache):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """add an item to the cache using a key"""
        if key is not None or item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCache.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}\n")

    def get(self, key):
        """retrieve an item from the cache using a key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
