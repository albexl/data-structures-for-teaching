from typing import Callable

from .base import BaseSortTest
from algorithms.sorting.mergesort import RecursiveMergeSort, IterativeMergeSort


class TestRecursiveMergeSort(BaseSortTest):
    @classmethod
    def setUpSortingInstance(cls, comp_func: Callable[[int, int], bool]):
        cls.sorting_instance = RecursiveMergeSort[int](comp_func)


class TestIterativeMergeSort(BaseSortTest):
    @classmethod
    def setUpSortingInstance(cls, comp_func: Callable[[int, int], bool]):
        cls.sorting_instance = IterativeMergeSort[int](comp_func)
