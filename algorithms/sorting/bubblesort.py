"""Module with the implementation of the BubbleSort algorithm."""


from .sort import Sort


class BubbleSort(Sort):
    """Class that represents a BubbleSort implementation."""

    def _sort(self, items):
        size = len(items)
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, size):
                if not self._comp_func(items[i - 1], items[i]):
                    items[i - 1], items[i] = items[i], items[i - 1]
                    swapped = True
            size -= 1
        return items
