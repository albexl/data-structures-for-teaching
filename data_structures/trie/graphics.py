from implementation import Trie

trie = Trie(["a", "b", "c", "d", "e"])
trie.insert("abc")
trie.insert("abcde")
trie.insert("bde")
trie.insert("bdac")

graph = trie.get_visual_representation()
graph.write_png("data_structures/trie/output.png")
