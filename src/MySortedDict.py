# src/MySortedDict.py

from typing import Optional
from sortedcontainers import SortedSet
from .Entry import Entry, K, V
from .BaseDict import BaseDict


class MySortedDict(BaseDict[K, V]):
    """
    A sorted dictionary implementation backed by a SortedSet.

    Entries are stored in sorted order based on their keys.
    """

    def __init__(self):
        """
        Initializes an empty MySortedDict.

        Example::
            my_dict = MySortedDict()
        """
        self.__entries: SortedSet[Entry[K, V]] = SortedSet()  # type: ignore

    # ---------- storage ----------

    def _get_entry(self, key: K) -> Optional[Entry[K, V]]:
        """
        Returns the entry associated with the given key.

        Args:
            key: The key to search for.

        Returns:
            The matching entry, or None if the key is not found.

        Example::
            my_dict = MySortedDict()
            my_dict['a'] = 1
            entry = my_dict._get_entry('a')
        """
        result: Optional[Entry[K, V]] = None
        probe = Entry(key, None)
        idx = self.__entries.bisect_left(probe)

        if idx < len(self.__entries):
            entry: Entry[K, V] = self.__entries[idx]  # type: ignore
            if entry.key == key:
                result = entry
        return result

    def _add_entry(self, entry: Entry[K, V]) -> None:
        """
        Adds an entry to the dictionary.

        Args:
            entry: The entry to add.

        Example::
            my_dict = MySortedDict()
            my_dict._add_entry(Entry('a', 1))
        """
        self.__entries.add(entry)

    def _remove_entry(self, entry: Entry[K, V]) -> None:
        """
        Removes an entry from the dictionary.

        Args:
            entry: The entry to remove.

        Example::
            my_dict = MySortedDict()
            my_dict['a'] = 1
            entry = my_dict._get_entry('a')
            my_dict._remove_entry(entry)
        """
        self.__entries.remove(entry)

    def _entries(self):
        """
        Returns an iterable over all entries in the dictionary.

        Returns:
            An iterable of all entries.

        Example::
            my_dict = MySortedDict()
            my_dict['a'] = 1
            my_dict['b'] = 2
            entries = my_dict._entries()
        """
        return self.__entries

    def __len__(self) -> int:
        """
        Returns the number of entries in the dictionary.

        Returns:
            The number of entries.

        Example::
            my_dict = MySortedDict()
            my_dict['a'] = 1
            my_dict['b'] = 2
            count = len(my_dict)
        """
        return len(self.__entries)

    # ---------- sorted-specific ----------

    def bisect_left(self, key: K) -> int:
        """
        Returns the index where the key would be inserted on the left.

        Args:
            key: The key to locate.

        Returns:
            The insertion index.

        Example::
            my_dict = MySortedDict()
            my_dict['a'] = 1
            my_dict['b'] = 2
            index = my_dict.bisect_left('a')
        """
        return self.__entries.bisect_left(Entry(key, None))

    def bisect_right(self, key: K) -> int:
        """
        Returns the index where the key would be inserted on the right.

        Args:
            key: The key to locate.

        Returns:
            The insertion index.

        Example::
            my_dict = MySortedDict()
            my_dict['a'] = 1
            my_dict['b'] = 2
            index = my_dict.bisect_right('a')
        """
        return self.__entries.bisect_right(Entry(key, None))

    def peekitem(self, ind: int) -> tuple[K, V]:
        """
        Returns the key-value pair at the given index.

        Args:
            ind: The index of the item.

        Returns:
            A (key, value) tuple.

        Raises:
            IndexError: If the index is out of range.

        Example::
            my_dict = MySortedDict()
            my_dict['a'] = 1
            my_dict['b'] = 2
            item = my_dict.peekitem(0)
        """
        size: int = self.__len__()

        if ind < -size or ind >= size:
            raise IndexError("index out of range")

        entry: Entry[K, V] = self.__entries[ind]  # type: ignore
        return entry.key, entry.value
