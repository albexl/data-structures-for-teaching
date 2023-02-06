from typing import Callable

from .base import BaseSortTest
from algorithms.sorting.quicksort import QuickSort


class TestQuickSort(BaseSortTest):
    @classmethod
    def setUpSortingInstance(cls, comp_func: Callable[[int, int], bool]):
        cls.sorting_instance = QuickSort[int](comp_func)
