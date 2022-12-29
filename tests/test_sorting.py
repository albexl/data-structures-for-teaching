"""Module to test the Sorting algorithms."""


from unittest import TestCase

from algorithms.sorting.bubblesort import BubbleSort
from algorithms.sorting.heapsort import HeapSort
from algorithms.sorting.mergesort import MergeSort


class TestSort(TestCase):
    """Base class to test Sorting implementations."""

    __test__ = False

    def setUp(self):
        self.items = None
        self.expected_result = None
        self.sorter = None

    def test_sorting(self):
        """Checks the sorting method is correct."""
        sorted_items = self.sorter.sort()
        self.assertEqual(sorted_items, self.expected_result)


class TestMergeSort(TestSort):
    """Class to test the Merge Sort implementation."""

    __test__ = True

    def setUp(self):
        self.items = [2, 4, 1, 4, 3, 9, 2, 1]
        self.expected_result = [1, 1, 2, 2, 3, 4, 4, 9]
        self.sorter = MergeSort(lambda x, y: x < y, self.items)


class TestBubbleSort(TestSort):
    """Class to test the Bubble Sort implementation."""

    __test__ = True

    def setUp(self):
        self.items = [2, 4, 1, 4, 3, 9, 2, 1]
        self.expected_result = [1, 1, 2, 2, 3, 4, 4, 9]
        self.sorter = BubbleSort(lambda x, y: x < y, self.items)


class TestHeapSort(TestSort):
    """Class to test the Bubble Sort implementation."""

    __test__ = True

    def setUp(self):
        self.items = [2, 4, 1, 4, 3, 9, 2, 1]
        self.expected_result = [1, 1, 2, 2, 3, 4, 4, 9]
        self.sorter = HeapSort(lambda x, y: x < y, self.items)
