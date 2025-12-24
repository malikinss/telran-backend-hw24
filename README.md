# HW24: Custom Dictionary Implementations and Cache

## Task Definition

In this homework, you will implement and test custom dictionary-like classes in Python. You will also extend the standard `OrderedDict` to implement a cache with eviction logic. The goal is to practice working with Python data structures, generics, and algorithmic complexity considerations.

You will work with the following classes:

-   `MyDict[K, V]`: A basic dictionary using a set of entries.
-   `MySortedDict[K, V]`: A sorted dictionary using `SortedSet`.
-   `DictCache[K, V]`: A cache extending `OrderedDict` with a maximum size and least-recently-used (LRU) eviction.

---

### 1. `MyDict[K, V]`

This class stores dictionary entries in a `set` of `Entry` objects.

#### Tasks

1. Implement the following magic and utility methods:

    - `__len__(self)` – return the number of entries.
    - `setdefault(self, key: K, default: V = None)` – if `key` is missing, insert `key: default`; return the value.
    - `get(self, key: K, default: V = None)` – return the value if key exists, else return default.
    - `keys(self) -> list[K]` – return a list of all keys.
    - `values(self) -> list[V]` – return a list of all values.
    - `update(self, key: K, value: V)` – update value if key exists, else insert key-value.
    - `pop(self, key: K, default=_sentinel) -> V` – remove key and return value; handle default if key missing.

2. Ensure your implementation uses `Entry` objects consistently and respects key uniqueness.

3. Write a separate test file to validate `MyDict`.

---

### 2. `MySortedDict[K, V]`

This class stores entries in a `SortedSet` and should have logarithmic complexity for key operations.

#### Tasks

1. Implement the following methods, ensuring `O(log N)` complexity where indicated:

    - `__getitem__(self, key: K) -> V`
    - `__setitem__(self, key: K, value: V)`
    - `__len__(self)`
    - `setdefault(self, key: K, default: V = None)`
    - `get(self, key: K, default: V = None)`
    - `keys(self) -> list[K]`
    - `values(self) -> list[V]`
    - `update(self, key: K, value: V)`
    - `pop(self, key: K, default=_sentinel) -> V`
    - `bisect_left(self, key: K) -> int` – first index of key ≥ given key.
    - `bisect_right(self, key: K) -> int` – first index of key > given key.
    - `peekitem(self, ind: int) -> tuple[K, V]` – return key-value tuple at index; support negative indexing.

2. Write a separate test file to validate `MySortedDict`.

---

### 3. `DictCache[K, V]`

This class extends `OrderedDict` to implement a cache with a maximum size and LRU eviction policy.

#### Tasks

1. Override the following methods:

    - `__getitem__(self, key)` – move accessed item to the end to mark it as most recently used.
    - `__setitem__(self, key, value)` – insert/update an item; evict least recently used item if cache exceeds `maxsize`.

2. Use the following hints:

    - `super().__getitem__(key)` – access `OrderedDict` method.
    - `super().__setitem__(key, value)` – set item in `OrderedDict`.
    - `self.move_to_end(key)` – move key to the most recent position.
    - `self.popitem(last=False)` – remove the eldest item.

3. Ensure all tests in `test_dict_cache.py` pass.

---

### Notes

-   Use the `Entry` dataclass provided for storing key-value pairs in `MyDict` and `MySortedDict`.
-   Implementations should strictly follow the TODO comments.
-   Pay attention to algorithmic complexity hints (`O(N)` vs `O(log N)`).
-   Tests should cover all implemented methods and edge cases.

---

### Deliverables

1. `main.py` – implementation of `MyDict`, `MySortedDict`, and `DictCache`.
2. `tests/test_mydict.py` – tests for `MyDict`.
3. `tests/test_mysorteddict.py` – tests for `MySortedDict`.
4. Ensure that `test_dict_cache.py` passes without modification.

## 📝 Description

This project implements custom Python dictionary structures with extended functionality:

-   `MyDict` for simple dictionary operations.
-   `MySortedDict` for sorted key operations with logarithmic complexity.
-   `DictCache` for LRU-style caching with a maximum size limit.

## 🎯 Purpose

-   Practice working with Python generics and custom data structures.
-   Implement dictionary-like behavior and caching logic.
-   Learn testing strategies for custom collections.

## 🔍 How It Works

-   `MyDict` uses a `set` of `Entry` objects for storage.
-   `MySortedDict` uses `SortedSet` for sorted storage and efficient key lookups.
-   `DictCache` extends `OrderedDict` to implement LRU eviction and maintain recent usage order.

## 📜 Output Example

```python
my_dict = MyDict()
my_dict['a'] = 1
my_dict['b'] = 2
print(my_dict.get('a'))  # Output: 1
```

```python
cache = DictCache(maxsize=2)
cache['x'] = 10
cache['y'] = 20
cache['z'] = 30  # 'x' is removed due to maxsize
```

## 📦 Usage

1. Clone the repository.
2. Implement missing methods according to TODOs.
3. Run tests to validate implementations.

## 🧪 Running Tests

```bash
python -m unittest discover -s tests -v
```

## ✅ Dependencies

-   Python 3.10+
-   `sortedcontainers` package

## 🗂 Project Structure

```
.
├── main.py
├── src
│   ├── __init__.py
│   ├── BaseDict.py
│   ├── DictCache.py
│   ├── Entry.py
│   ├── MyDict.py
│   └── MySortedDict.py
└── tests
    ├── __init__.py
    ├── test_dict_cache.py
    ├── test_my_dict.py
    ├── test_my_dict_common.py
    └── test_my_sorted_dict.py
```

## 📊 Project Status

✅ Implemented `MyDict`, `MySortedDict`, and `DictCache`
✅ All unit tests passing
🔄 Ready for further extensions or optimizations

## 📄 License

MIT License

---

## 🧮 Conclusion

This homework demonstrates the creation of custom dictionary-like data structures in Python and LRU caching, along with comprehensive unit testing.

---

Made with ❤️ and `Python` by **Sam-Shepsl Malikin** 🎓
© 2025 All rights reserved.
