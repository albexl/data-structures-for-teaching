"""Module to generate visual representations of tries."""

import typer

from .implementation import Trie


def create_png(output_directory: str):

    trie = Trie(["a", "b", "c", "d", "e"])
    trie.insert("abc")
    trie.insert("b")
    trie.insert("abc")
    trie.insert("abcde")
    trie.insert("bde")
    trie.insert("bdac")

    graph = trie.get_visual_representation()
    graph.write_png(output_directory)


if __name__ == "__main__":
    typer.run(create_png)
