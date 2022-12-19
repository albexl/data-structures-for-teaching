"""Module to test the Trie implementations."""


from unittest import TestCase

from data_structures.trie.implementation import Trie


class TestTrie(TestCase):
    """Class to test the Trie implementation."""

    def setUp(self):
        self.trie = Trie(["a, b, c"])

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

    def test_count_insertions_word_not_inserted(self):
        """Checks that the count of words that haven't been inserted is 0."""
        self.trie.insert("abc")
        self.assertEqual(self.trie.count_insertions("xyz"), 0)

    def test_count_insertions(self):
        """Checks inserted words are counted the correct number of times."""
        self.trie.insert("abc")
        self.trie.insert("abc")
        self.trie.insert("a")
        self.assertEqual(self.trie.count_insertions("abc"), 2)
        self.assertEqual(self.trie.count_insertions("a"), 1)
        self.assertEqual(self.trie.count_insertions("ab"), 0)
