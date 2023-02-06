"""Module with the implementation of the InsertionSort algorithm."""


from typing import List

from .sort import Sort, T


class InsertionSort(Sort[T]):
    """Class that represents an InsertionSort implementation."""

    def _sort(self, items: List[T]) -> List[T]:
        size = len(items)
        sorted_items = items.copy()

        for i in range(1, size):
            j = i
            while j > 0 and self._comp_func(sorted_items[j], sorted_items[j - 1]):
                sorted_items[j], sorted_items[j - 1] = (
                    sorted_items[j - 1],
                    sorted_items[j],
                )
                j = j - 1

        return sorted_items
