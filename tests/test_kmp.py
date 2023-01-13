"""Module to test the KMP implementations."""

from typing import List
from unittest import TestCase

from parameterized import parameterized

from algorithms.searching.kmp import KMP


class TestKMP(TestCase):
    """Class to test the KMP implementation."""

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
        """Checks find occurrences are found. Assumes indexing at 1."""
        kmp = KMP(self.text, pattern)
        self.assertEqual(kmp.find_occurrences(), expected)
