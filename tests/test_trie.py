from unittest import TestCase

from data_structures.trie.implementation import Trie


class TestTrie(TestCase):

    def setUp(self):
        self.trie = Trie(['a, b, c'])

    def test_search_before_insert(self):
        self.assertFalse(self.trie.search("abc"))

    def test_search_after_insert(self):
        self.trie.insert("abc")
        self.trie.insert("ab")
        self.assertTrue(self.trie.search("abc"))
        self.assertTrue(self.trie.search("ab"))
        self.assertFalse(self.trie.search("a"))

    def test_search_prefix(self):
        self.trie.insert("abc")
        self.assertTrue(self.trie.search_prefix("a"))
        self.assertTrue(self.trie.search_prefix("ab"))
        self.assertTrue(self.trie.search_prefix("abc"))
