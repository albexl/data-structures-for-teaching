"""Module to test the Sorting algorithms."""


from unittest import TestCase

from algorithms.sorting.mergesort import MergeSort


class TestMergeSort(TestCase):
    """Class to test the Merge Sort implementation."""

    def setUp(self):
        self.items = [2, 4, 1, 4, 3, 9, 2, 1]
        self.sorter = MergeSort(lambda x, y: x < y, self.items)

    def test_sorting(self):
        """Checks the sorting method is correct."""
        sorted_items = self.sorter.sort()
        self.assertEqual(sorted_items, [1, 1, 2, 2, 3, 4, 4, 9])
