#!/usr/bin/python3

"""
Basic cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching
    """

    def put(self, key, item):
        """
        Add an item in the cache

        Args:
            key: key of the item
            item: value of the item
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key

        Args:
            key: key of the item

        Returns:
            The value linked to the key or None
        """
        if key is None:
            return None

        return self.cache_data.get(key)
