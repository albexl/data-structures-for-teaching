from typing import Callable

from algorithms.sorting.heapsort import HeapSort

from .base import BaseSortTest


class TestHeapSort(BaseSortTest):
    __test__ = True

    @classmethod
    def setUpSortingInstance(cls, comp_func: Callable[[int, int], bool]):
        cls.sorting_instance = HeapSort[int](comp_func)
