# src/MyDict.py

from typing import Iterable, Optional
from .Entry import Entry, K, V
from .BaseDict import BaseDict


class MyDict(BaseDict[K, V]):
    """
    A simple dictionary implementation using a set to store entries.

    Inherits from BaseDict and provides implementations for the abstract
    methods defined there.
    """
    def __init__(self):
        """
        Initializes an empty MyDict.

        Example::
            my_dict = MyDict()
        """
        self.__entries: set[Entry] = set()

    # ---------- implementation of methods ----------

    def _get_entry(self, key: K) -> Optional[Entry[K, V]]:
        """
        Returns the entry associated with the given key.

        Args:
            key: The key to search for.

        Returns:
            The entry associated with the key, or None if the key
            is not found.

        Example::
            my_dict = MyDict()
            my_dict['a'] = 1
            entry = my_dict._get_entry('a')
        """
        probe = Entry(key, None)
        if probe in self.__entries:
            return next(e for e in self.__entries if e == probe)
        return None

    def _add_entry(self, entry: Entry[K, V]) -> None:
        """
        Adds the given entry to the dictionary.

        Args:
            entry: The entry to add.

        Example::
            my_dict = MyDict()
            my_dict._add_entry(Entry('a', 1))
        """
        self.__entries.add(entry)

    def _remove_entry(self, entry: Entry[K, V]) -> None:
        """
        Removes the given entry from the dictionary.

        Args:
            entry: The entry to remove.

        Example::
            my_dict = MyDict()
            my_dict['a'] = 1
            entry = my_dict._get_entry('a')
            my_dict._remove_entry(entry)
        """
        self.__entries.remove(entry)

    def _entries(self) -> Iterable[Entry[K, V]]:
        """
        Returns an iterable over all entries in the dictionary.

        Returns:
            An iterable of all entries in the dictionary.

        Example::
            my_dict = MyDict()
            my_dict['a'] = 1
            my_dict['b'] = 2
            entries = my_dict._entries()
        """
        return self.__entries

    def __len__(self) -> int:
        """
        Returns the number of entries in the dictionary.

        Returns:
            The number of entries in the dictionary.

        Example::
            my_dict = MyDict()
            my_dict['a'] = 1
            my_dict['b'] = 2
            count = len(my_dict)
        """
        return len(self.__entries)
