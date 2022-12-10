"""Module to test the Union Find implementations."""


from unittest import TestCase

from data_structures.union_find.implementation import WeightedQuickUnion


class TestWeightedQuickUnion(TestCase):
    """Class to test the WeightedQuickUnion implementation."""

    def setUp(self):
        self.union_find = WeightedQuickUnion(5)

    def test_connected_with_self(self):
        """Check that every node is connected to itself."""
        for i in range(self.union_find.size):
            self.assertTrue(self.union_find.connected(i, i))

    def test_connected_with_other(self):
        """Check that different nodes are not connected."""
        for i in range(self.union_find.size):
            for j in range(self.union_find.size):
                if i != j:
                    self.assertFalse(self.union_find.connected(i, j))

    def test_connected_after_union(self):
        """Check two nodes are connected after performing the "union" operation."""
        self.union_find.union(0, 1)
        self.assertTrue(self.union_find.connected(0, 1))
