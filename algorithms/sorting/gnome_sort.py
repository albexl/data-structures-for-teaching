"""Module with the implementation of the GnomeSort algorithm."""

from typing import List

from .sort import Sort


class GnomeSort(Sort):
    """Class that represents a GnomeSort implementation."""

    def _sort(self, items: List) -> List:
        sorted_items = items.copy()
        pos = 0
        while pos < len(items):
            if pos == 0 or self._comp_func(sorted_items[pos - 1], sorted_items[pos]):
                pos += 1
            else:
                sorted_items[pos], sorted_items[pos - 1] = (
                    sorted_items[pos - 1],
                    sorted_items[pos],
                )
                pos -= 1
        return sorted_items
