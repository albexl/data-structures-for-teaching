"""Module with the implementation of the Linear Search algorithm."""

from .search import Search


class LinearSearch(Search):
    """Class that represents a Linear Search implementation."""

    def search(self, item) -> int:
        for i, _item in enumerate(self._items):
            if self._comp_func(_item, item):
                return i
        return -1
