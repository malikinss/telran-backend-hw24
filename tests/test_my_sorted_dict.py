# tests/test_my_sorted_dict.py

import unittest

from src import MySortedDict
from .test_my_dict_common import TestMyDictCommon


class TestMySortedDict(TestMyDictCommon):
    """
    Concrete test suite for the `MySortedDict` implementation.

    Inherits all common dictionary behavior tests and
    adds tests for sorted-specific functionality.
    """

    def get_dict(self):
        """
        Returns a new instance of `MySortedDict` for testing.
        """
        return MySortedDict()

    def test_bisect_left(self):
        """
        Test bisect_left behavior for existing and non-existing keys.
        """
        test_dict = self._prepare_dict()
        test_data = [
            ("a", 0),
            ("d", 3),
            ("A", 0),
        ]

        for key, expected in test_data:
            print(
                f"Testing bisect_left for key='{key}'"
                ", expecting index={expected}"
            )
            with self.subTest(key=key):
                self.assertEqual(expected, test_dict.bisect_left(key))

    def test_bisect_right(self):
        """
        Test bisect_right behavior for existing and non-existing keys.
        """
        test_dict = self._prepare_dict()
        test_data = [
            ("a", 1),
            ("c", 3),
            ("d", 3),
            ("A", 0),
        ]

        for key, expected in test_data:
            print(
                f"Testing bisect_right for key='{key}', "
                "expecting index={expected}"
            )
            with self.subTest(key=key):
                self.assertEqual(expected, test_dict.bisect_right(key))

    def test_peekitem_valid_indexes(self):
        """
        Test peekitem with valid positive and negative indexes.
        """
        test_dict = self._prepare_dict()
        test_data = [
            (0, ("a", 1)),
            (1, ("b", 2)),
            (2, ("c", 3)),
            (-1, ("c", 3)),
            (-2, ("b", 2)),
            (-3, ("a", 1)),
        ]

        for index, expected in test_data:
            print(
                f"Testing peekitem for index={index}, "
                "expecting value={expected}"
            )
            with self.subTest(index=index):
                self.assertEqual(expected, test_dict.peekitem(index))

    def test_peekitem_invalid_indexes(self):
        """
        Test peekitem with out-of-range indexes raises IndexError.
        """
        test_dict = self._prepare_dict()
        test_data = [3, -4]

        for index in test_data:
            print(f"Testing peekitem with invalid index={index}")
            with self.subTest(index=index):
                with self.assertRaises(IndexError):
                    test_dict.peekitem(index)


if __name__ == "__main__":
    print("Running MySortedDict tests...")
    unittest.main()
