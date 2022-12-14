"""Module to test the Stack implementations."""


from unittest import TestCase

from data_structures.stack.implementation import ArrayBasedStack, LinkedStack


class BaseTestStack(TestCase):
    """Base class to test Stack implementation."""

    __test__ = False

    def setUp(self):
        self.stack = None
        self.test_items = None

    def test_empty_stack(self):
        """Checks stack is empty when just created."""
        self.assertTrue(self.stack.is_empty())

    def test_push_and_pop(self):
        """Check the stack returns the elements in the reverse order they were added."""
        for item in self.test_items:
            self.stack.push(item)
        retrieved_items = []
        while not self.stack.is_empty():
            retrieved_items.append(self.stack.pop())
        self.assertEqual(retrieved_items, list(reversed(self.test_items)))


class TestArrayBaseStack(BaseTestStack):
    """Class to test the ArrayBasedStack implementation."""

    __test__ = True

    def setUp(self):
        self.stack = ArrayBasedStack()
        self.test_items = [1, 2, 3]


class TestLinkedStack(BaseTestStack):
    """Class to test the LinkedStack implementation."""

    __test__ = True

    def setUp(self):
        self.stack = LinkedStack()
        self.test_items = [1, 2, 3]
