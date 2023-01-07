"""Module with the implementation of the BubbleSort algorithm."""


from typing import List

from .sort import Sort


class BubbleSort(Sort):
    """Class that represents a BubbleSort implementation."""

    def _sort(self, items: List) -> List:
        size = len(items)
        swapped = True
        sorted_items = items.copy()
        while swapped:
            swapped = False
            for i in range(1, size):
                if not self._comp_func(sorted_items[i - 1], sorted_items[i]):
                    sorted_items[i - 1], sorted_items[i] = (
                        sorted_items[i],
                        sorted_items[i - 1],
                    )
                    swapped = True
            size -= 1
        return sorted_items
