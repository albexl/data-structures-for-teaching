"""Module with the implementation of the Lineal Search algorithm."""

from .search import Search


class LinealSearch(Search):
    """Class that represents a Lineal Search implementation."""

    def search(self, item) -> int:
        for i in range(0, len(self._items)):
            _item = self._items[i]
            if self._comp_func(_item, item) == 0:
                return i
        return -1
