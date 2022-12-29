"""Module with the implementation of the MergeSort algorithm."""


class MergeSort:
    """Class that represents a MergeSort implementation."""

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
        if len(items) <= 1:
            return items

        left = items[0 : len(items) // 2]
        right = items[len(items) // 2 : len(items)]

        left = self._sort(left)
        right = self._sort(right)

        sorted_items = self._merge(left, right)
        return sorted_items

    def _merge(self, left, right):
        merged = []
        left_idx = 0
        right_idx = 0

        while left_idx < len(left) and right_idx < len(right):
            if self._comp_func(left[left_idx], right[right_idx]):
                merged.append(left[left_idx])
                left_idx += 1
            else:
                merged.append(right[right_idx])
                right_idx += 1

        while left_idx < len(left):
            merged.append(left[left_idx])
            left_idx += 1

        while right_idx < len(right):
            merged.append(right[right_idx])
            right_idx += 1

        return merged
