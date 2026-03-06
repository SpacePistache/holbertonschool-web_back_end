#!/usr/bin/python3
"""
LRU Cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching
    and implements the LRU caching
    """

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """Add item in the cache using LRU style"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage.remove(key)

        self.cache_data[key] = item
        self.usage.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = self.usage.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        # mark as recently used
        self.usage.remove(key)
        self.usage.append(key)

        return self.cache_data[key]
