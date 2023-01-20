"""Module with the implementation of the naive algorithm for pattern searching."""


from typing import List

from .base_string import StringSearch


class Naive(StringSearch):
    """Class implementation of the naive string algorithm."""

    def __init__(self, text: str, pattern: str) -> None:
        super().__init__(text=text, pattern=pattern)
        self._text = text
        self._pattern = pattern

    def find_occurrences(self) -> List:

        occurrences = []

        for i in range(len(self._text) - len(self._pattern) + 1):

            j = 0
            while j < len(self._pattern):
                if self._text[i + j] != self._pattern[j]:
                    break
                j += 1

            if j == len(self._pattern):
                occurrences.append(i + 1)

        return occurrences
