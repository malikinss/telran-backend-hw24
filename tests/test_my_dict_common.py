# tests/test_my_dict_common.py

import unittest


class TestMyDictCommon(unittest.TestCase):
    """
    Common unit tests for dictionary-like implementations.

    These tests verify basic dictionary behavior such as:
        - Setting and updating items
        - Default values
        - Retrieving keys, values, and items
        - Removing items
        - Accessing missing keys
    """

    def get_dict(self):
        """
        Factory method for dictionary under test.
        Must be implemented by subclasses.
        """
        raise NotImplementedError()

    def _prepare_dict(self):
        if self.__class__ is TestMyDictCommon:
            self.skipTest("Base test class")

        test_dict = self.get_dict()
        test_dict["a"] = 1
        test_dict["b"] = 2
        test_dict["c"] = 3
        return test_dict

    def test_set_and_update(self):
        """
        Test setting and updating existing and new items.
        """
        test_data = [
            # Existing key via assignment and update
            (
                "a",
                [("set", 20), ("update", 40)],
                40,
            ),

            # New key via assignment
            (
                "d",
                [("set", 20)],
                20,
            ),

            # New key via update
            (
                "e",
                [("update", 40)],
                40,
            ),
        ]

        for key, operations, expected in test_data:
            print(
                f"Testing set/update for key='{key}', "
                f"operations={operations}, expecting={expected}"
            )
            with self.subTest(key=key, operations=operations):
                test_dict = self._prepare_dict()

                for op, value in operations:
                    if op == "set":
                        test_dict[key] = value
                    elif op == "update":
                        test_dict.update(key, value)

                self.assertEqual(expected, test_dict[key])

    def test_setdefault(self):
        """
        Test setdefault behavior for existing and new keys.
        """
        test_data = [
            # Existing key
            ("a", 40, 1),

            # New key
            ("d", 40, 40),
        ]

        for key, default, expected in test_data:
            print(
                f"Testing setdefault for key='{key}', "
                f"default={default}, expecting={expected}"
            )
            with self.subTest(key=key):
                test_dict = self._prepare_dict()
                result = test_dict.setdefault(key, default)

                self.assertEqual(expected, result)
                self.assertEqual(expected, test_dict[key])

    def test_items_keys_values(self):
        """
        Test items(), keys(), and values() methods.
        """
        test_dict = self._prepare_dict()

        test_data = [
            (
                "items",
                sorted(test_dict.items()),
                [("a", 1), ("b", 2), ("c", 3)],
            ),
            (
                "keys",
                sorted(test_dict.keys()),
                ["a", "b", "c"],
            ),
            (
                "values",
                sorted(test_dict.values()),
                [1, 2, 3],
            ),
        ]

        for name, actual, expected in test_data:
            print(f"Testing {name}(), expecting {expected}")
            with self.subTest(method=name):
                self.assertEqual(expected, actual)

    def test_pop(self):
        """
        Test pop behavior for existing and non-existing keys.
        """
        test_data = [
            # Existing key
            ("a", None, 1, False),

            # Non-existing key with default
            ("d", None, None, True),
        ]

        for key, default, expected, should_exist in test_data:
            print(
                f"Testing pop for key='{key}', "
                f"default={default}, expecting={expected}"
            )
            with self.subTest(key=key):
                test_dict = self._prepare_dict()
                result = test_dict.pop(key, default)

                self.assertEqual(expected, result)
                if not should_exist:
                    self.assertIsNone(test_dict.get(key))

        # Non-existing key without default → KeyError
        test_dict = self._prepare_dict()
        with self.assertRaises(KeyError):
            test_dict.pop("d")

    def test_get_and_access(self):
        """
        Test get() and [] access for existing and missing keys.
        """
        test_data = [
            # Existing key
            ("a", 1),

            # Missing key via get
            ("d", None),
        ]

        for key, expected in test_data:
            print(f"Testing get for key='{key}', expecting={expected}")
            with self.subTest(key=key):
                test_dict = self._prepare_dict()
                self.assertEqual(expected, test_dict.get(key))

        # Missing key via [] → KeyError
        test_dict = self._prepare_dict()
        with self.assertRaises(KeyError):
            _ = test_dict["d"]


if __name__ == "__main__":
    print("Running MyDict common tests...")
    unittest.main()
