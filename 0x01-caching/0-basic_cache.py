#!/usr/bin/env python3
"""basic cache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """create basic caching system"""
    def __init__(self):
        """initialize the class"""
        super().__init__()

    def put(self, key, item):
        """add key to the cache"""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get item from the cache """
        cache_data = self.cache_data
        if key not in cache_data or key is None:
            return None
        return cache_data[key]
