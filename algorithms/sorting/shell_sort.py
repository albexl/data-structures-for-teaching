"""Module with the implementation of the ShellSort algorithm."""


from typing import Callable, List

from .sort import Sort


class ShellSort(Sort):
    """Class that represents a ShellSort implementation."""

    def __init__(self, func: Callable, items: List, gap_list: List[int]):
        super().__init__(func, items)
        self.gap_list = gap_list

    def _sort(self, items: List) -> List:
        sorted_items = items.copy()
        for gap in self.gap_list:
            for i in range(gap, len(items)):
                temp = sorted_items[i]
                j = i
                while j >= gap and not self._comp_func(sorted_items[j - gap], temp):
                    sorted_items[j] = sorted_items[j - gap]
                    j -= gap
                sorted_items[j] = temp
        return sorted_items
