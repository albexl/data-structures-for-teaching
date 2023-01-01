"""Union Find implementations."""

from abc import ABC, abstractmethod


class UnionFind(ABC):
    """Base class for Union Find implementation."""

    def __init__(self, size: int):
        self.size = size
        self.ids = list(range(size))

    @abstractmethod
    def connected(self, node_a: int, node_b: int) -> bool:
        """Checks if `node_a` and `node_b` belong to the same
        connected component.

        Args:
            node_a (int): Node to check.
            node_b (int): Node to check.

        Returns:
            bool: True if `node_a` and `node_b` belong to the same component,
            False otherwise.
        """

    @abstractmethod
    def union(self, node_a: int, node_b: int):
        """Joins `node_a` and `node_b`, making them both
        be a part of the same connected component.

        Args:
            node_a (int): Node to join.
            node_b (int): Node to join.
        """


class QuickFind(UnionFind):
    """An alternative to solve the dynamic connectivity problem.

    connected(): O(1)
    union(): O(n)
    """

    def connected(self, node_a: int, node_b: int) -> bool:
        return self.ids[node_a] == self.ids[node_b]

    def union(self, node_a: int, node_b: int):
        root_a = self.ids[node_a]
        root_b = self.ids[node_b]

        for i, _ in enumerate(self.ids):
            if self.ids[i] == root_a:
                self.ids[i] = root_b


class QuickUnion(UnionFind):
    """An alternative to solve the dynamic connectivity problem.

    root(): O(n)
    connected(): O(n)
    union(): O(n)
    """

    def connected(self, node_a: int, node_b: int):
        return self._root(node_a) == self._root(node_b)

    def union(self, node_a: int, node_b: int):
        root_a = self._root(node_a)
        root_b = self._root(node_b)
        self.ids[root_a] = root_b

    def _root(self, node: int) -> int:
        while node != self.ids[node]:
            node = self.ids[node]
        return node


class WeightedQuickUnion(QuickUnion):
    """An alternative to solve the dynamic connectivity problem.

    root(): O(log n)
    connected(): O(log n)
    union(): O(log n)
    """

    def __init__(self, size: int):
        super().__init__(size)
        self.sizes = [1] * size

    def union(self, node_a: int, node_b: int):
        root_a = self._root(node_a)
        root_b = self._root(node_b)
        if root_a == root_b:
            return

        if self.sizes[root_a] > self.sizes[root_b]:
            root_a, root_b = root_b, root_a

        self.sizes[root_b] += self.sizes[root_a]
        self.ids[root_a] = root_b
