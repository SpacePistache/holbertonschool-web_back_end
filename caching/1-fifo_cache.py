#!/usr/bin/python3

#!/usr/bin/python3
"""
FIFO Cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class inheriting from BaseCaching
    and implementing the FIFO caching algorithm
    """

    def __init__(self):
        """Initialization"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache using FIFO rules
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            old_key = self.order.pop(0)
            del self.cache_data[old_key]
            print("DISCARD:", old_key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None:
            return None

        return self.cache_data.get(key)
