# tests/test_dict_cache.py

import unittest
from src import DictCache


class TestDictCache(unittest.TestCase):
    """
    Unit tests for the `DictCache` class.

    These tests verify LRU-like behavior:
        - Removing the eldest item on overflow
        - Updating access order on get
        - Updating access order on set
    """

    def test_cache_behavior(self):
        """
        Test multiple cache behavior scenarios.

        This includes:
            - Inserting a new item removes the eldest
            - Accessing an item updates its recency
            - Updating an item updates its recency
        """
        test_data = [
            # Insert exceeds capacity, eldest removed
            (
                ["a", "b"],          # initial keys
                [("c", 30)],         # operations
                "a",                 # expected removed key
                {"b": 2, "c": 30},   # expected remaining items
            ),

            # Access updates order, then insert removes the other key
            (
                ["a", "b"],
                [("get", "a"), ("c", 30)],
                "b",
                {"a": 1, "c": 30},
            ),

            # Update updates order, then insert removes the other key
            (
                ["a", "b"],
                [("a", 10), ("c", 30)],
                "b",
                {"a": 10, "c": 30},
            ),
        ]

        for initial_keys, operations, removed_key, expected_items in test_data:
            print(
                f"Testing initial keys: {initial_keys}, "
                f"operations: {operations}, "
                f"expecting removal of: '{removed_key}', "
                f"remaining items: {expected_items}"
            )
            with self.subTest(
                initial_keys=initial_keys,
                operations=operations
            ):
                cache: DictCache[str, int] = DictCache(2)

                # Initial population
                for key in initial_keys:
                    cache[key] = 1 if key == "a" else 2

                # Apply operations
                for op in operations:
                    if op[0] == "get":
                        _ = cache[op[1]]
                    else:
                        cache[op[0]] = op[1]

                # Removed key should raise KeyError
                with self.assertRaises(KeyError):
                    _ = cache[removed_key]

                # Remaining items should match expected values
                for key, value in expected_items.items():
                    self.assertEqual(cache[key], value)


if __name__ == "__main__":
    print("Running DictCache tests...")
    unittest.main()
