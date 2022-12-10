from unittest import TestCase

from data_structures.stack.implementation import ArrayBasedStack, LinkedStack


class BaseTestStack(TestCase):

    __test__ = False

    def setUp(self):
        self.stack = None
        self.test_item = None

    def test_empty_stack(self):
        self.assertTrue(self.stack.is_empty())

    def test_push_and_pop(self):
        self.stack.push(self.test_item)
        self.assertEqual(self.test_item, self.stack.pop())


class TestArrayBaseStack(BaseTestStack):

    __test__ = True

    def setUp(self):
        self.stack = ArrayBasedStack()
        self.test_item = 5


class TestLinkedStack(BaseTestStack):

    __test__ = True

    def setUp(self):
        self.stack = LinkedStack()
        self.test_item = 5
