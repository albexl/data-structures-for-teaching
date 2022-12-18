"""Module to test the Trie implementations."""


from unittest import TestCase

from data_structures.trie.implementation import Trie


class TestTrie(TestCase):
    """Class to test the Trie implementation."""

    def setUp(self):
        self.trie = Trie(['a, b, c'])

    def test_search_before_insert(self):
        """Checks no word is found when just created."""
        self.assertFalse(self.trie.search("abc"))

    def test_search_true_after_insert(self):
        """Checks inserted words are found."""
        self.trie.insert("abc")
        self.trie.insert("ab")
        self.assertTrue(self.trie.search("abc"))
        self.assertTrue(self.trie.search("ab"))

    def test_search_false_after_insert(self):
        """Checks not inserted words are not found."""
        self.trie.insert("abc")
        self.trie.insert("ab")
        self.assertFalse(self.trie.search("a"))
        self.assertFalse(self.trie.search("ac"))

    def test_search_prefix(self):
        """Checks prefix search of the inserted words."""
        self.trie.insert("abc")
        self.assertTrue(self.trie.search_prefix("a"))
        self.assertTrue(self.trie.search_prefix("ab"))
        self.assertTrue(self.trie.search_prefix("abc"))
