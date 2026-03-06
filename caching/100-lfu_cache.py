#!/usr/bin/python3
"""
LFU Cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.freq = {}
        self.usage = []

    def put(self, key, item):
        """Add item using LFU policy"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            self.usage.remove(key)
            self.usage.append(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.freq.values())

            candidates = []
            for k in self.freq:
                if self.freq[k] == min_freq:
                    candidates.append(k)

            discard = None
            for k in self.usage:
                if k in candidates:
                    discard = k
                    break

            del self.cache_data[discard]
            del self.freq[discard]
            self.usage.remove(discard)

            print("DISCARD:", discard)

        self.cache_data[key] = item
        self.freq[key] = 1
        self.usage.append(key)

    def get(self, key):
        """Retrieve item"""
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        self.usage.remove(key)
        self.usage.append(key)

        return self.cache_data[key]
