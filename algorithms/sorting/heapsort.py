"""Module with the implementation of the HeapSort algorithm."""


from typing import List

from data_structures.heap.implementation import Heap

from .sort import Sort


class HeapSort(Sort):
    """Class that represents a HeapSort implementation."""

    def _sort(self, items: List) -> List:
        heap = Heap(self._comp_func)
        for item in items:
            heap.insert(item)
        return [heap.pop() for _ in range(len(items))]
