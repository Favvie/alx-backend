#!/usr/bin/env python3
"""basic cache"""
import math
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    MAX_ITEMS = math.inf

    def put(self, key, item):
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        cache_data = self.cache_data
        if key not in cache_data or key is None:
            return None
        return cache_data[key]
