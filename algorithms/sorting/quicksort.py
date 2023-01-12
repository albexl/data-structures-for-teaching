"""Module with the implementation of the QuickSort algorithm."""


from typing import List, Callable
from random import randint

from .sort import Sort


class QuickSort(Sort):
    """Class that represents a QuickSort implementation."""

    def __init__( self, func: Callable, items: List, pivot_strategy: Callable = None ) -> None:
        super().__init__(func, items)
        
        if pivot_strategy == None:
            pivot_strategy = lambda l, r: randint(l, r)
        self.pivot_strategy = pivot_strategy 


    def _sort(self, items: List) -> List:
        size = len(items)
        sorted_items = items.copy()

        self.__sort(sorted_items, 0, size - 1)
        return sorted_items

    def __sort(self, items: List, p: int, r: int) -> None:
        if r <= p:
            return

        q = self.__partition(items, p, r)

        self.__sort(items, p, q)
        self.__sort(items, q + 1, r)

    def __partition(self, items: List, p: int, r: int) -> int:

        piv = items[self.pivot_strategy(p, r)]
        i = p
        j = r

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
