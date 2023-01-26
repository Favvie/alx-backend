#!/usr/bin/env python3
"""fifo caching optimization"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """create a fifo caching system"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """add key to the cache"""
        cache = self.cache_data
        if key is not None and item is not None:
            cache[key] = item
            if len(cache) > BaseCaching.MAX_ITEMS:
                print('DISCARD: ' + list(cache)[0])
                cache.pop(list(cache)[0])

    def get(self, key):
        """ Returns the item on the cache linked to key """
        cache = self.cache_data
        if key not in cache or key is None:
            return None
        return cache[key]
