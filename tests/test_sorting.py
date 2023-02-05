"""Module to test the Sorting algorithms."""

from random import randint
from unittest import TestCase

from parameterized import parameterized

from algorithms.sorting.bogo_sort import BogoSort
from algorithms.sorting.bubble_sort import BubbleSort
from algorithms.sorting.counting_sort import CountingSort
from algorithms.sorting.heap_sort import HeapSort
from algorithms.sorting.insertion_sort import InsertionSort
from algorithms.sorting.merge_sort import IterativeMergeSort, RecursiveMergeSort
from algorithms.sorting.quick_sort import QuickSort
from algorithms.sorting.selection_sort import SelectionSort
from algorithms.sorting.shell_sort import ShellSort


class TestSort(TestCase):
    """Base class to test Sorting implementations."""

    @parameterized.expand(
        [
            (
                BogoSort,
                lambda x, y: x < y,
                [2, 4, 1],
                [1, 2, 4],
            ),
            (
                CountingSort,
                lambda x, y: x["key"] < y["key"],
                [
                    {"key": 3, "value": "item1"},
                    {"key": 2, "value": "item2"},
                    {"key": 3, "value": "item3"},
                    {"key": 1, "value": "item4"},
                ],
                [
                    {"key": 1, "value": "item4"},
                    {"key": 2, "value": "item2"},
                    {"key": 3, "value": "item1"},
                    {"key": 3, "value": "item3"},
                ],
            ),
            (
                BubbleSort,
                lambda x, y: x < y,
                [2, 4, 1, 4, 3, 9, 2, 1],
                [1, 1, 2, 2, 3, 4, 4, 9],
            ),
            (
                SelectionSort,
                lambda x, y: x < y,
                [2, 4, 1, 4, 3, 9, 2, 1],
                [1, 1, 2, 2, 3, 4, 4, 9],
            ),
            (
                InsertionSort,
                lambda x, y: x > y,
                [2, 4, 1, 4, 3, 9, 2, 1],
                [9, 4, 4, 3, 2, 2, 1, 1],
            ),
            (
                HeapSort,
                lambda x, y: x < y,
                [2, 4, 1, 4, 3, 9, 2, 1],
                [1, 1, 2, 2, 3, 4, 4, 9],
            ),
            (
                RecursiveMergeSort,
                lambda x, y: x["value"] < y["value"],
                [
                    {"name": "item1", "value": 100},
                    {"name": "item2", "value": 10},
                    {"name": "item3", "value": 25},
                ],
                [
                    {"name": "item2", "value": 10},
                    {"name": "item3", "value": 25},
                    {"name": "item1", "value": 100},
                ],
            ),
            (
                IterativeMergeSort,
                lambda x, y: x["value"] < y["value"],
                [
                    {"name": "item1", "value": 100},
                    {"name": "item2", "value": 10},
                    {"name": "item3", "value": 25},
                ],
                [
                    {"name": "item2", "value": 10},
                    {"name": "item3", "value": 25},
                    {"name": "item1", "value": 100},
                ],
            ),
        ]
        + [
            (
                IterativeMergeSort,
                lambda x, y: x < y,
                list(range(n, 0, -1)),
                list(range(1, n + 1)),
            )
            for n in range(2, 33)
        ]
        + [
            (
                RecursiveMergeSort,
                lambda x, y: x < y,
                list(range(n, 0, -1)),
                list(range(1, n + 1)),
            )
            for n in range(2, 33)
        ]
    )
    def test_sorting(self, sorting_method, comp_func, items, expected):
        """Checks the sorting method works correctly.

        Args:
            sorting_method (Sort): The sorting method to test.
            comp_func (func): The comparison function used by the sorting method.
            items (List): The items to sort.
            expected (List): The expected order of the items after sorting.
        """
        original_items = items.copy()
        sorter = sorting_method(comp_func, items)
        sorted_items = sorter.sort()
        self.assertEqual(sorted_items, expected)
        self.assertEqual(original_items, items)


class TestShellSort(TestCase):
    """Class to test the Shell Sort implementation"""

    @parameterized.expand(
        [
            (
                lambda x, y: x < y,
                [2, 4, 1, 4, 3, 9, 2, 1],
                [1, 1, 2, 2, 3, 4, 4, 9],
                [701, 301, 132, 57, 23, 10, 4, 1],
            )
        ]
    )
    def test_sorting(self, comp_func, items, expected, gap_list):
        """Checks the sorting method works correctly.

        Args:
            comp_func (func): The comparison function used by the sorting method.
            items (List): The items to sort.
            expected (List): The expected order of the items after sorting.
            gap_list(List[int]): Gap list required for Shell Sort.
        """
        original_items = items.copy()
        sorter = ShellSort(comp_func, items, gap_list)
        sorted_items = sorter.sort()
        self.assertEqual(sorted_items, expected)
        self.assertEqual(original_items, items)


class TestQuickSort(TestCase):
    """Class to test the Quick Sort implementation"""

    @parameterized.expand(
        [
            (
                lambda x, y: x > y,
                [2, 4, 1, 4, 3, 9, 2, 1],
                [9, 4, 4, 3, 2, 2, 1, 1],
                lambda l, r: randint(l, r),
            ),
            (
                lambda x, y: x["value"] < y["value"],
                [
                    {"name": "item1", "value": 100},
                    {"name": "item2", "value": 10},
                    {"name": "item3", "value": 25},
                ],
                [
                    {"name": "item2", "value": 10},
                    {"name": "item3", "value": 25},
                    {"name": "item1", "value": 100},
                ],
                lambda l, r: int((l + r) / 2),
            ),
        ]
    )
    def test_sorting(self, comp_func, items, expected, pivot_strategy):
        """Checks the sorting method works correctly.

        Args:
            comp_func (func): The comparison function used by the sorting method.
            items (List): The items to sort.
            expected (List): The expected order of the items after sorting.
            pivot_strategy(func): Strategy pivot for the QuickSort algorithm.
        """
        original_items = items.copy()
        sorter = QuickSort(comp_func, items, pivot_strategy)
        sorted_items = sorter.sort()
        self.assertEqual(sorted_items, expected)
        self.assertEqual(original_items, items)
