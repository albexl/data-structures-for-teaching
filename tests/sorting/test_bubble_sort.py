from typing import Callable

from algorithms.sorting.bubblesort import BubbleSort

from .base import BaseSortTest


class TestBubbleSort(BaseSortTest):
    __test__ = True

    @classmethod
    def setUpSortingInstance(cls, comp_func: Callable[[int, int], bool]):
        cls.sorting_instance = BubbleSort[int](comp_func)
