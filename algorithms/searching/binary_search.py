"""Module with the implementation of the Binary Search algorithm."""

from .search import Search


class BinarySearch(Search):
    """Class that represents a Binary Search implementation."""

    def search(self, item) -> int:
        low = 0
        high = len(self._items) - 1
        while low <= high:
            mid = (low + high)//2
            if self._comp_func(item, self._items[mid]) < 0:
                high = mid - 1
            elif self._comp_func(item, self._items[mid]) > 0:
                low = mid + 1
            else:
                return mid

        return -1
