from typing import Callable

from .base import BaseSortTest
from algorithms.sorting.bubblesort import BubbleSort


class TestBubbleSort(BaseSortTest):
    __test__ = True

    @classmethod
    def setUpSortingInstance(cls, comp_func: Callable[[int, int], bool]):
        cls.sorting_instance = BubbleSort[int](comp_func)
