"""Implementation of the Base classes for string algorithms."""

from abc import ABC, abstractmethod
from typing import List


class StringSearch(ABC):
    """Base class for string search algorithms."""

    def __init__(self, text: str, pattern: str) -> None:
        """
        Class constructor.

        Parameters
        ----------
        text : str
            String on which the search is performed.
        pattern : str
            Pattern to search in the text.
        """
        self.text = text
        self.pattern = pattern

    @abstractmethod
    def find_occurrences(self) -> List:
        """Find the occurrences of the pattern in the text.
        Assumes indexing starting at 1.

        Returns:
            List: List with the occurrences of the pattern in the text.
        """
