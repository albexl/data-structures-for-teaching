"""Module with the implementation of the HeapSort algorithm."""


from typing import Generic, List

from data_structures.heap.implementation import Heap

from .sort import Sort, T


class HeapSort(Sort[T]):
    """Class that represents a HeapSort implementation."""

    def _sort(self, items: List[T]) -> List[T]:
        heap = Heap(self._comp_func)
        for item in items:
            heap.insert(item)
        return [heap.pop() for _ in range(len(items))]
