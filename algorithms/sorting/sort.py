"""Module with the base implementation of a Sort class."""


class Sort:
    """Base class for sorting."""

    def __init__(self, func, items):
        self._comp_func = func
        self._items = items

    def sort(self):
        """Returns the sorted version of the elements contained
        in the `_items` property.

        Returns:
            List: The sorted elements.
        """
        return self._sort(self._items)

    def _sort(self, items):
        pass
