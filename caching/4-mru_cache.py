#!/usr/bin/python3
"""
MRU Cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """Add item using MRU policy"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage.remove(key)

        if (key not in self.cache_data and
                len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            mru_key = self.usage.pop()
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        self.cache_data[key] = item
        self.usage.append(key)

    def get(self, key):
        """Retrieve item"""
        if key is None or key not in self.cache_data:
            return None

        self.usage.remove(key)
        self.usage.append(key)

        return self.cache_data[key]
