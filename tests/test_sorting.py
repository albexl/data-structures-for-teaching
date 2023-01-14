"""Module to test the Sorting algorithms."""


from unittest import TestCase

from parameterized import parameterized

from algorithms.sorting.bubblesort import BubbleSort
from algorithms.sorting.heapsort import HeapSort
from algorithms.sorting.insertionsort import InsertionSort
from algorithms.sorting.mergesort import IterativeMergeSort, RecursiveMergeSort
from algorithms.sorting.selectionsort import SelectionSort
from algorithms.sorting.quicksort import QuickSort


class TestSort(TestCase):
    """Base class to test Sorting implementations."""

    @parameterized.expand(
        [
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
            (
                QuickSort,
                lambda x, y: x > y,
                [2, 4, 1, 4, 3, 9, 2, 1],
                [9, 4, 4, 3, 2, 2, 1, 1],
            ),
            (
                QuickSort,
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
                lambda a, b: int((a + b) / 2),
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
    def test_sorting(
        self, sorting_method, comp_func, items, expected, pivot_strategy=None
    ):
        """Checks the sorting method works correctly.

        Args:
            sorting_method (Sort): The sorting method to test.
            comp_func (func): The comparison function used by the sorting method.
            items (List): The items to sort.
            expected (List): The expected order of the items after sorting.
            pivot_strategy(funt): Strategy pivot of QuickSort algorithm.
        """
        original_items = items.copy()

        sorter = None
        if pivot_strategy == None:
            sorter = sorting_method(comp_func, items)
        else:
            sorter = sorting_method(comp_func, items, pivot_strategy)

        sorted_items = sorter.sort()
        self.assertEqual(sorted_items, expected)
        self.assertEqual(original_items, items)
