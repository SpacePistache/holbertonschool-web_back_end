#!/usr/bin/python3
"""
LIFO Cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class from BaseCaching
    and implements the LIFO caching algorithm
    """

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache using LIFO principles
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.order[-2]
            del self.cache_data[last_key]
            self.order.remove(last_key)
            print("DISCARD:", last_key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None:
            return None

        return self.cache_data.get(key)
