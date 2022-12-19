"""Module with Trie implementations."""


class TrieNode:
    """Class that represents a node in the Trie."""

    def __init__(self, alphabet, symbol):
        self.alphabet = alphabet
        self.symbol = symbol
        self.final = False
        self.edges = {}
        self.cnt = 0

    def add_edge(self, symbol: str):
        """Adds an edge between the node and a new node
        with the symbol supplied.

        Args:
            symbol (str): The symbol of the new node.

        Returns:
            TrieNode: The new node.
        """
        self.edges[symbol] = TrieNode(self.alphabet, symbol)
        return self.edges[symbol]

    def get_node(self, symbol: str):
        """Returns the adjacent node with the symbol supplied.

        Args:
            symbol (str): The symbol to look for the node.

        Returns:
            TrieNode: The adjacent node. None in case it doesn't exist.
        """
        return self.edges.get(symbol, None)


class Trie:
    """Class that represents a Trie."""

    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.root = TrieNode(alphabet, '^')

    def insert(self, word: str):
        """Inserts a word in the Trie.

        Args:
            word (str): The word to be inserted.
        """
        cur_node = self.root
        for symbol in word:
            next_node = cur_node.get_node(symbol)
            if next_node is None:
                next_node = cur_node.add_edge(symbol)
            cur_node = next_node
        cur_node.cnt += 1
        cur_node.final = True

    def search(self, word: str) -> bool:
        """Checks if the word supplied is present in the trie.

        Args:
            word (str): The word to look for.

        Returns:
            bool: True if the word is found, False otherwise.
        """
        return self.count_insertions(word) > 0

    def search_prefix(self, word: str) -> bool:
        """Checks if the word supplied is a prefix
        of some word in the Trie.

        Args:
            word (str): The word to check for prefix.

        Returns:
            bool: True if "word" is prefix of some other word in the Trie, False otherwise.
        """
        cur_node = self.root
        for symbol in word:
            next_node = cur_node.get_node(symbol)
            if next_node is None:
                return False
            cur_node = next_node
        return True

    def count_insertions(self, word: str) -> int:
        """Counts the number of times the word supplied
        has been inserted in the Trie.

        Args:
            word (str): The word to count insertions.

        Returns:
            int: The number of times `word` has been inserted in the Trie.
        """
        cur_node = self.root
        for symbol in word:
            next_node = cur_node.get_node(symbol)
            if next_node is None:
                return 0
            cur_node = next_node
        return cur_node.cnt
