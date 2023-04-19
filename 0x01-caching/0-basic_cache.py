#!/usr/bin/env ptyhon3
"""basic cache module"""
BaseCache = __import__('base_caching').BaseCaching


class BasicCache(BaseCache):
    """Basic cache class that inherits from BaseCache"""

    def put(self, key, item):
        """add an item to the cache using a key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """retrieve an item from the cache using a key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
