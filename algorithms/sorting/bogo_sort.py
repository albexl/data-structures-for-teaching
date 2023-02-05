"""Module with the implementation of the BogoSort algorithm."""

from random import shuffle
from typing import List

from .sort import Sort


class BogoSort(Sort):
    """Class that represents a BogoSort implementation."""

    def _is_sorted(self, items) -> bool:
        return all(self._comp_func(a, b) for a, b in zip(items, items[1:]))

    def _sort(self, items: List) -> List:
        sorted_items = items.copy()
        while not self._is_sorted(sorted_items):
            shuffle(sorted_items)
        return sorted_items
