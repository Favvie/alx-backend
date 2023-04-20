#!/usr/bin/env python3
"""LFU caching algorithm module"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFU Caching algorithm class"""
    def __init__(self) -> None:
        super().__init__()
        self.useCount = {}

    def put(self, key, item):
        """Add item to cache using lfu strategy"""
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data.pop(key)
            data = {
                key: item
            }
            self.cache_data = {**data, **self.cache_data}
            if key in self.useCount:
                self.useCount[key] += 1
            else:
                self.useCount[key] = 0
            print(f'useCount: {self.useCount}')

            if len(self.cache_data) > self.MAX_ITEMS:
                # min_used = min(self.useCount.values())
                useCountLast = list(self.useCount.values())
                useCountLast = useCountLast[:-1]
                min_used = min(useCountLast)
                # print(f"min_used: {min_used}")
                leastUsedKeys = [key for key in self.useCount.keys() if
                                 self.useCount[key] == min_used]
                leastUsedKeys = leastUsedKeys[:-1]

                # print(f"leastusedkeys: {leastUsedKeys}")

                if len(leastUsedKeys) > 1:
                    lruItem = leastUsedKeys[0]
                    self.cache_data.pop(lruItem)
                    self.useCount.pop(lruItem)
                    print(f'DISCARD: {lruItem}')
                elif len(leastUsedKeys) == 1:
                    self.cache_data.pop(leastUsedKeys[0])
                    self.useCount.pop(leastUsedKeys[0])
                    print(f'DISCARD: {leastUsedKeys[0]}')
                elif len(leastUsedKeys) == 0:
                    print('empty leastused keys')

    def get(self, key):
        """Get item from cache with lfu strategy"""
        if key is None or key not in self.cache_data:
            return None
        if key in self.cache_data.keys():
            count = self.useCount[key]
        count += 1
        self.useCount[key] = count
        return self.cache_data[key]
