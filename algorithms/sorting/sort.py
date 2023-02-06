"""Module with the base implementation of a Sort class."""

from abc import ABC, abstractmethod
from typing import Callable, List, Generic, TypeVar


T = TypeVar("T")

class Sort(ABC, Generic[T]):
    """Base class for sorting."""

    def __init__(self, comp_func: Callable[[T, T], bool]) -> None:
        self._comp_func = comp_func

    def sort(self, items: List) -> List:
        """Returns the sorted version of the elements contained
        in the `_items` property.

        Returns:
            List: The sorted elements.
        """
        return self._sort(items)

    @abstractmethod
    def _sort(self, items: List) -> List:
        """Abstract method that should be implemented on
        the concrete classes that inherit from `Sort`.

        It should sort the `items` collection using a specific
        sorting method.

        Args:
            items (List): The collection to sort.

        Returns:
            List: The sorted version of the `items` list.
        """
