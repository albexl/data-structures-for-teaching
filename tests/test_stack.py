"""Module to test the Stack implementations."""


from unittest import TestCase

from data_structures.stack.implementation import ArrayBasedStack, LinkedStack


class BaseTestStack(TestCase):
    """Base class to test Stack implementation."""

    __test__ = False

    def setUp(self):
        self.stack = None
        self.test_item = None

    def test_empty_stack(self):
        """Checks stack is empty when just created."""
        self.assertTrue(self.stack.is_empty())

    def test_push_and_pop(self):
        """Checks that the "pop" method returns the value just added by the "push" method"""
        self.stack.push(self.test_item)
        self.assertEqual(self.test_item, self.stack.pop())


class TestArrayBaseStack(BaseTestStack):
    """Class to test the ArrayBasedStack implementation."""

    __test__ = True

    def setUp(self):
        self.stack = ArrayBasedStack()
        self.test_item = 5


class TestLinkedStack(BaseTestStack):
    """Class to test the LinkedStack implementation."""

    __test__ = True

    def setUp(self):
        self.stack = LinkedStack()
        self.test_item = 5
