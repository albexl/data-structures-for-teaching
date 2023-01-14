"""Module with the base implementation of a Search class."""

from abc import ABC, abstractmethod
from typing import Callable, List


class Search(ABC):
    """Base class for searching."""

    def __init__(self, func: Callable, items: List) -> None:
        self._comp_func = func
        self._items = items

    @abstractmethod
    def search(self, item) -> int:
        """Abstract method that should be implemented on
        the concrete classes that inherit from `Search`.

        It should search for an ocurrence of the item in the collection.

        Args:
            item: The item to search for.

        Returns:
            int: The index where the item is found.
        """
