# https://docs.python.org/3/library/unittest.html

import unittest
from main import sum


class TestsMain(unittest.TestCase):
    def test_sum(self):
        assert sum(1, 1) == 2


if __name__ == "__main__":
    unittest.main()
