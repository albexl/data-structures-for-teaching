from math import sqrt
from unittest import TestCase

from algorithms.binary_search.binarysearch import BinarySearchBase


class TestBinarySearch(TestCase):
    def setUp(self) -> None:
        self.array = list(2 ** i for i in range(10))

    def test_upper_bound_array(self):
        """Checks that we can find the first element strictly greater that x in an array."""
        n = len(self.array)

        search = BinarySearchBase(lambda x: self.array[x] > 4)
        self.assertEqual(search(0, n), 3)

        search = BinarySearchBase(lambda x: self.array[x] > 512)
        self.assertEqual(search(0, n), 10)

        search = BinarySearchBase(lambda x: self.array[x] > 0)
        self.assertEqual(search(0, n), 0)

    def test_lower_bound_array(self):
        """Checks that we can find the first element greater than or equal to x in an array"""
        n = len(self.array)

        search = BinarySearchBase(lambda x: self.array[x] >= 4)
        self.assertEqual(search(0, n), 2)

        search = BinarySearchBase(lambda x: self.array[x] >= 513)
        self.assertEqual(search(0, n), 10)

        search = BinarySearchBase(lambda x: self.array[x] >= 0)
        self.assertEqual(search(0, n), 0)

    def test_floating_point_search(self):
        search = BinarySearchBase(lambda x: x * x > 2)
        result = search(left=0,right=2,stop_length=1e-6,floating_division=True)
        self.assertLess(abs(result - sqrt(2)), 1e-6)


