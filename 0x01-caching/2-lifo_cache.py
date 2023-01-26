#!/usr/bin/env python3
""" lifo caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Defines a caching system using the LIFO cache replacement algorithm """
    def __init__(self):
        """ Initializes the class """
        super().__init__()

    def put(self, key, item):
        """ Adds data to the cache """
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data.pop(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key_del = list(self.cache_data)[-2]
                self.cache_data.pop(key_del)
                print("DISCARD: {}".format(key_del))

    def get(self, key):
        """ Returns the item on the cache linked to key """
        cache = self.cache_data
        if key not in cache or key is None:
            return None
        return cache[key]
