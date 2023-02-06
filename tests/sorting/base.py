"""Module holding base and common code for test sorting algorithms."""

from typing import List
from unittest import TestCase
from abc import ABCMeta, abstractmethod

from algorithms.sorting.sort import Sort


class BaseSortTest(TestCase, metaclass=ABCMeta):
    """Base class to test Sorting implementations."""
    __test__= False

    @classmethod
    @abstractmethod
    def setUpSortingInstance(cls, comp_func):
        """Set up the sorting class to be used in the tests.

        The field `sorting_instance` should be set to an instance inheriting from the 
        `algorithms.sorting.sort.Sort` class
        """
        # raise NotImplementedError

    @classmethod
    def setUpClass(cls):
        print("Setting up class")
        cls.setUpSortingInstance(lambda x, y: x < y)

    def assertSorting(self, sorting_instance: Sort, items: List, expected: List):
        """Assert that the sorting algorithm returns the expected result."""
        original_items = items.copy()

        self.assertEqual(sorting_instance.sort(items), expected)
        self.assertEqual(items, original_items)

    def test_sort__should_return_empty_list_when_items_empty(self):
        """Test the sorting algorithm with an empty list."""
        self.assertSorting(self.sorting_instance, [], [])

    def test_sort__should_return_single_item_list_when_single_item_is_provided(self):
        """Test the sorting algorithm with a single item."""
        self.assertSorting(self.sorting_instance, [1], [1])

    def test_sort__should_keep_order_when_items_already_sorted(self):
        """Test the sorting algorithm with a list already sorted."""
        sorted_elements = [1,2,3,4,5,6,7,8,9,10]
        self.assertSorting(self.sorting_instance, sorted_elements, sorted_elements)

    def test_sort__should_sort_items_when_items_reversed_sort(self):
        """Test the sorting algorithm with a list reverse sorted."""
        sorted_elements = [1,2,3,4,5,6,7,8,9,10]
        self.assertSorting(
            self.sorting_instance, sorted_elements[::-1], sorted_elements
        )

    def test_sort__should_sort_when_items_contains_duplicates(self):
        """Test the sorting algorithm with a list with duplicates."""
        duplicated_unsorted = [2,1,2,3,1,5]
        duplicated_sorted = [1,1,2,2,3,5]
        self.assertSorting(
            self.sorting_instance, duplicated_unsorted, duplicated_sorted
        )
