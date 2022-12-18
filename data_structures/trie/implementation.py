class TrieNode:

    def __init__(self, alphabet, symbol):
        self.alphabet = alphabet
        self.symbol = symbol
        self.final = False
        self.edges = {}

    def add_edge(self, symbol):
        self.edges[symbol] = TrieNode(self.alphabet, symbol)
        return self.edges[symbol]

    def get_node(self, symbol):
        return self.edges.get(symbol, None)


class Trie:
    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.root = TrieNode(alphabet, '^')

    def insert(self, word):
        cur_node = self.root
        for symbol in word:
            next_node = cur_node.get_node(symbol)
            if next_node is None:
                next_node = cur_node.add_edge(symbol)
            cur_node = next_node
        cur_node.final = True

    def search(self, word):
        cur_node = self.root
        for symbol in word:
            next_node = cur_node.get_node(symbol)
            if next_node is None:
                return False
            cur_node = next_node
        return cur_node.final

    def search_prefix(self, word):
        cur_node = self.root
        for symbol in word:
            next_node = cur_node.get_node(symbol)
            if next_node is None:
                return False
            cur_node = next_node
        return True
