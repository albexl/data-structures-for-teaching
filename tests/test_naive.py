"""Module to test the naive algorithm implementations."""

from typing import List
from unittest import TestCase

from parameterized import parameterized

from algorithms.strings.naive import Naive


class TestNaive(TestCase):
    """Class to test the naive algorithm implementation."""

    def setUp(self):
        self.text = "abcdeaaabbbecdabdecbecccadccdbdedddabc"

    @parameterized.expand(
        [
            ("a", [1, 6, 7, 8, 15, 25, 36]),
            ("abc", [1, 36]),
            ("cc", [22, 23, 27]),
            ("bde", [16, 30]),
            ("bbb", [9]),
            ("xyz", []),
        ]
    )
    def test_find_occurrences(self, pattern: str, expected: List[int]):
        """Checks occurrences are found correctly. Assumes indexing at 1."""
        naive = Naive(self.text, pattern)
        self.assertEqual(naive.find_occurrences(), expected)
