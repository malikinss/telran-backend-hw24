# src/Entry.py

from typing import Generic, TypeVar, Hashable
from dataclasses import dataclass, field

# K is bound to Hashable to ensure keys can be used in hash-based collections
K = TypeVar("K", bound=Hashable)

# V can be any type
V = TypeVar("V")


@dataclass(order=True, frozen=True)
class Entry(Generic[K, V]):
    """
    Represents a key-value pair.

    Attributes:
        key: The key of the entry.
        value: The value associated with the key.
    """

    key: K
    value: V = field(compare=False, hash=False)

    def __hash__(self) -> int:
        """
        Returns the hash of the entry.

        The hash is based solely on the key.

        Returns:
            The hash value of the key.
        """
        return hash(self.key)

    def __str__(self) -> str:
        """
        Returns a string representation of the entry.

        Returns:
            A string in the format "'key': value".
        """
        return f"'{self.key}': {self.value}"
