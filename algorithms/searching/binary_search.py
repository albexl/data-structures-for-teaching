"""Module with the implementation of the Binary Search algorithm."""

from .search import Search


class BinarySearch(Search):
    """Class that represents a Binary Search implementation."""

    def search(self, item) -> int:
        l = 0
        r = len(self._items) - 1

        while l <= r:
            mid = int((l + r) / 2)
            mid_item = self._items[mid]

            if self._comp_func(mid_item, item) == 0:
                return mid

            if l == r:
                return -1

            if self._comp_func(item, mid_item) < 0:
                r = mid - 1
            else:
                l = mid + 1

        return -1
