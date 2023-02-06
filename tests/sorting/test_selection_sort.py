from typing import Callable

from .base import BaseSortTest
from algorithms.sorting.selectionsort import SelectionSort


class TestSelectionSort(BaseSortTest):
    @classmethod
    def setUpSortingInstance(cls, comp_func: Callable[[int, int], bool]):
        cls.sorting_instance = SelectionSort[int](comp_func)
