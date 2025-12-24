# src/BaseDict.py

from abc import ABC, abstractmethod
from typing import Iterable, Optional, Generic
from .Entry import Entry, K, V


class BaseDict(ABC, Generic[K, V]):
    """
    Abstract base class for a dictionary-like data structure.

    This class provides common dictionary behavior and enforces the
    implementation of storage-specific methods in subclasses.
    """

    # --- sentinel for missing default values ---
    _sentinel = object()

    # --- abstract methods to be implemented by subclasses ---

    @abstractmethod
    def _get_entry(self, key: K) -> Optional[Entry[K, V]]:
        """
        Returns the entry associated with the given key.
        Args:
            key: The key to search for.
        Returns:
            The entry if found, otherwise None.
        Example::
            entry = self._get_entry('a')
        """
        pass

    @abstractmethod
    def _add_entry(self, entry: Entry[K, V]) -> None:
        """
        Adds an entry to the internal storage.
        Args:
            entry: The entry to add.
        Example::
            self._add_entry(Entry('a', 1))
        """
        pass

    @abstractmethod
    def _remove_entry(self, entry: Entry[K, V]) -> None:
        """
        Removes an entry from the internal storage.
        Args:
            entry: The entry to remove.
        Example::
            self._remove_entry(Entry('a', 1))
        """
        pass

    @abstractmethod
    def _entries(self) -> Iterable[Entry[K, V]]:
        """
        Returns an iterable over all stored entries.
        Returns:
            An iterable of entries.
        Example::
            for entry in self._entries():
                print(entry)
        """
        pass

    # --- common dict helper methods ---

    @staticmethod
    def _value_or_default(
        entry: Optional[Entry[K, V]], default: Optional[V]
    ) -> Optional[V]:
        """
        Returns the entry value or a default value.

        Args:
            entry: The entry to extract the value from.
            default: The value to return if entry is None.

        Returns:
            The entry value if present, otherwise the default value.

        Example::
            value = BaseDict._value_or_default(Entry('a', 1), 0)
            missing = BaseDict._value_or_default(None, 0)
        """
        return entry.value if entry is not None else default

    # --- common dict magic methods ---

    def __setitem__(self, key: K, value: V) -> None:
        """
        Sets the value for the given key.

        If the key already exists, its entry is replaced.

        Args:
            key: The key to set.
            value: The value to associate with the key.

        Example::
            my_dict['a'] = 1
        """
        entry: Optional[Entry[K, V]] = self._get_entry(key)
        if entry is not None:
            self._remove_entry(entry)
        self._add_entry(Entry(key, value))

    def __getitem__(self, key: K) -> V:
        """
        Returns the value associated with the given key.

        Args:
            key: The key to retrieve.

        Returns:
            The value associated with the key.

        Raises:
            KeyError: If the key is not found.

        Example::
            value = my_dict['a']
        """
        entry: Optional[Entry[K, V]] = self._get_entry(key)
        if entry is None:
            raise KeyError(key)
        return entry.value

    def __str__(self) -> str:
        """
        Returns a string representation of the dictionary.

        Returns:
            A string in the form "{'key1': value1, 'key2': value2, ...}".

        Example::
            str_repr = str(my_dict)
        """
        str_entries = (str(entry) for entry in self._entries())
        return "{" + ", ".join(str_entries) + "}"

    # --- common dict API ---

    def get(self, key: K, default: Optional[V] = None) -> Optional[V]:
        """
        Returns the value associated with the given key.

        Args:
            key: The key to search for.
            default: The value to return if the key is not found.

        Returns:
            The value associated with the key or the default value.

        Example::
            value = my_dict.get('a', 0)
        """
        return self._value_or_default(self._get_entry(key), default)

    def setdefault(self, key: K, default: Optional[V] = None) -> Optional[V]:
        """
        Returns the value for the given key, inserting a default if missing.

        Args:
            key: The key to search for.
            default: The value to insert if the key is not found.

        Returns:
            The value associated with the key.

        Example::
            value = my_dict.setdefault('a', 0)
        """
        entry: Optional[Entry[K, V]] = self._get_entry(key)
        if entry is None:
            self._add_entry(Entry(key, default))  # type: ignore
        return self._value_or_default(entry, default)

    def pop(self, key: K, default: Optional[V] = _sentinel) -> Optional[V]:
        """
        Removes the entry with the given key and returns its value.

        Args:
            key: The key to remove.
            default: The value to return if the key is not found.

        Returns:
            The removed value or the default value.

        Raises:
            KeyError: If the key is not found and no default is provided.

        Example::
            value = my_dict.pop('a')
        """
        entry: Optional[Entry[K, V]] = self._get_entry(key)

        if entry is None and default is self._sentinel:
            raise KeyError(key)

        if entry is not None:
            self._remove_entry(entry)

        return self._value_or_default(entry, default)

    def update(self, key: K, value: V) -> None:
        """
        Updates the value for the given key.

        Args:
            key: The key to update.
            value: The new value.

        Example::
            my_dict.update('a', 2)
        """
        old_entry: Optional[Entry[K, V]] = self._get_entry(key)
        if old_entry is not None:
            self._remove_entry(old_entry)
        self._add_entry(Entry(key, value))

    def items(self) -> list[tuple[K, V]]:
        """
        Returns a list of key-value pairs.

        Returns:
            A list of (key, value) tuples.

        Example::
            items = my_dict.items()
        """
        return [(e.key, e.value) for e in self._entries()]

    def keys(self) -> list[K]:
        """
        Returns a list of keys.

        Returns:
            A list of keys.

        Example::
            keys = my_dict.keys()
        """
        return [e.key for e in self._entries()]

    def values(self) -> list[V]:
        """
        Returns a list of values.

        Returns:
            A list of values.

        Example::
            values = my_dict.values()
        """
        return [e.value for e in self._entries()]
