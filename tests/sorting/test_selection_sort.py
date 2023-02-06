from typing import Callable

from algorithms.sorting.selectionsort import SelectionSort

from .base import BaseSortTest


class TestSelectionSort(BaseSortTest):
    @classmethod
    def setUpSortingInstance(cls, comp_func: Callable[[int, int], bool]):
        cls.sorting_instance = SelectionSort[int](comp_func)
