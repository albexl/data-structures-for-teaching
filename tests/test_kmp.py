"""Module to test the KMP implementations."""

from unittest import TestCase
from algorithms.searching.kmp import KMP


class TestKMP(TestCase):
    """Class to test the KMP implementation."""

    def setUp(self):
        self.text = 'abcdeaaabbbecdabdecbecccadccdbdedddabc'
        self.kmp1 = KMP(self.text, 'a')
        self.kmp2 = KMP(self.text, 'abc')
        self.kmp3 = KMP(self.text, 'cc')
        self.kmp4 = KMP(self.text, 'bde')
        self.kmp5 = KMP(self.text, 'bbb')

    def test_find_occurrences(self):
        """Checks find occurrences are found. Assumes indexing at 1."""
        self.assertEqual(self.kmp1.find_occurrences(),
                         [1, 6, 7, 8, 15, 25, 36])
        self.assertEqual(self.kmp2.find_occurrences(),
                         [1, 36])
        self.assertEqual(self.kmp3.find_occurrences(),
                         [22, 23, 27])
        self.assertEqual(self.kmp4.find_occurrences(),
                         [16, 30])
        self.assertEqual(self.kmp5.find_occurrences(),
                         [9])
