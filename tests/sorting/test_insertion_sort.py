from typing import Callable

from algorithms.sorting.insertionsort import InsertionSort

from .base import BaseSortTest


class TestInsertionSort(BaseSortTest):
    @classmethod
    def setUpSortingInstance(cls, comp_func: Callable[[int, int], bool]):
        cls.sorting_instance = InsertionSort[int](comp_func)
