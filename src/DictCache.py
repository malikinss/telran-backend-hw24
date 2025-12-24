# src/DictCache.py

from collections import OrderedDict
from .Entry import K, V


class DictCache(OrderedDict[K, V]):
    """
    A cache implementation based on OrderedDict.

    The cache maintains insertion order and limits the number of entries.
    When the cache exceeds its maximum size, the oldest entry is removed.
    Accessing an item marks it as the most recently used.

    Attributes:
        maxsize: Maximum number of entries allowed in the cache.
    """

    def __init__(self, maxsize: int = 128):
        """
        Initializes an empty DictCache.

        Args:
            maxsize: Maximum number of entries allowed in the cache.

        Example::
            my_cache = DictCache(maxsize=128)
        """
        super().__init__()
        self.maxsize = maxsize

    def __getitem__(self, key: K) -> V:
        """
        Returns the value associated with the given key.

        Accessing the key updates its position to the most recently used.

        Args:
            key: The key to retrieve.

        Returns:
            The value associated with the key.

        Raises:
            KeyError: If the key is not found in the cache.

        Example::
            value = my_cache[key]
        """
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key: K, value: V) -> None:
        """
        Sets the value for the given key in the cache.

        If the key already exists, its value is updated and the entry is
        moved to the most recently used position. If adding the new key
        exceeds the maximum cache size, the oldest entry is removed.

        Args:
            key: The key to set.
            value: The value to associate with the key.

        Example::
            my_cache[key] = value
        """
        exists = key in self
        super().__setitem__(key, value)
        self.move_to_end(key)

        if not exists and len(self) > self.maxsize:
            self.popitem(last=False)
