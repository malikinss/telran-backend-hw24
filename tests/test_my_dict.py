# tests/test_my_dict.py

import unittest

from src import MyDict
from .test_my_dict_common import TestMyDictCommon


class TestMyDict(TestMyDictCommon):
    """
    Concrete test suite for the `MyDict` implementation.

    Inherits all common dictionary behavior tests
    from `TestMyDictCommon`.
    """

    def get_dict(self):
        """
        Returns a new instance of `MyDict` for testing.
        """
        return MyDict()


if __name__ == "__main__":
    print("Running MyDict tests...")
    unittest.main()
