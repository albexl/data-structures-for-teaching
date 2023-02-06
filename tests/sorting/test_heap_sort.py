from typing import Callable
from .base import BaseSortTest
from algorithms.sorting.heapsort import HeapSort

class TestHeapSort(BaseSortTest):
    __test__= True

    @classmethod
    def setUpSortingInstance(cls, comp_func: Callable[[int, int], bool]):
        cls.sorting_instance = HeapSort[int](comp_func)