from typing import Callable

from .base import BaseSortTest
from algorithms.sorting.insertionsort import InsertionSort


class TestInsertionSort(BaseSortTest):
    @classmethod
    def setUpSortingInstance(cls, comp_func: Callable[[int, int], bool]):
        cls.sorting_instance = InsertionSort[int](comp_func)
