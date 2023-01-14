"""Module with the implementation of the QuickSort algorithm."""


from random import randint
from typing import Callable, List

from .sort import Sort


class QuickSort(Sort):
    """Class that represents a QuickSort implementation."""

    def __init__(
        self,
        func: Callable,
        items: List,
        pivot_strategy: Callable = lambda l, r: randint(l, r),
    ) -> None:
        super().__init__(func, items)
        self.pivot_strategy = pivot_strategy

    def _sort(self, items: List) -> List:
        size = len(items)
        sorted_items = items.copy()

        self.__sort(sorted_items, 0, size - 1)
        return sorted_items

    def __sort(self, items: List, left: int, right: int) -> None:
        if right <= left:
            return

        mid = self.__partition(items, left, right)

        self.__sort(items, left, mid)
        self.__sort(items, mid + 1, right)

    def __partition(self, items: List, left: int, right: int) -> int:

        piv = items[self.pivot_strategy(left, right)]
        i = left
        j = right

        while True:
            while self._comp_func(items[i], piv):
                i += 1

            while self._comp_func(piv, items[j]):
                j -= 1

            if i < j:
                items[i], items[j] = items[j], items[i]
                i += 1
                j -= 1
            else:
                return j
