from typing import Callable

from algorithms.sorting.quicksort import QuickSort

from .base import BaseSortTest


class TestQuickSort(BaseSortTest):
    @classmethod
    def setUpSortingInstance(cls, comp_func: Callable[[int, int], bool]):
        cls.sorting_instance = QuickSort[int](comp_func)
