"""Module with the implementation of the SelectionSort algorithm."""


from typing import List

from .sort import Sort, T


class SelectionSort(Sort):
    """Class that represents a SelectionSort implementation."""

    def _sort(self, items: List[T]) -> List[T]:
        size = len(items)
        sorted_items = items.copy()

        for i in range(size):
            min_index = i
            for j in range(i + 1, size):
                if self._comp_func(sorted_items[j], sorted_items[min_index]):
                    min_index = j

            sorted_items[i], sorted_items[min_index] = (
                sorted_items[min_index],
                sorted_items[i],
            )

        return sorted_items
