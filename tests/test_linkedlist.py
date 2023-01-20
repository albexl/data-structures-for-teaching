"""Module to test the LinkedList implementations."""

from unittest import TestCase

from data_structures.linked_list.implementation import LinkedList

class BaseTestLinkedList(TestCase):
    """Base class to test LinkedList implementation."""

    __test__ = False

    def setUp(self):
        self.linked_list = None
        self.test_items = []

    def test_empty_linkedlist(self):
        """Checks LinkedList is empty when just created."""
        self.assertTrue(self.linked_list.is_empty())

    def test_add_and_get(self):
        """Check the LinkedList returns the elements in the same order they were added."""
        for item in self.test_items:
            self.linked_list.add(item)
        retrieved_items = []
        for i in range(1, self.linked_list.length()):
            retrieved_items.append(self.linked_list.get(i))
        self.assertEqual(retrieved_items, self.test_items)

    def test_clear(self):
        """Check the LinkedList return no elements."""
        if not self.linked_list.is_empty():
            self.linked_list.clear()
            self.assertEqual(0, self.linked_list.length())
            self.assertTrue(self.linked_list.is_empty())
    
    def test_copy_to(self):
        aux_list = [4, 5]
        
        self.linked_list.copy_to(aux_list, -1)
        self.assertRaises(ValueError)
        
        self.linked_list.copy_to(aux_list, 100)
        self.assertRaises(ValueError)
        
        self.linked_list.copy_to(aux_list, 2)
        self.assertEqual(aux_list, [4, 5, 2, 3])

class TestLinkedList(BaseTestLinkedList):
    """Class to test the LinkedList implementation."""

    __test__ = True

    def setUp(self):
        self.linked_list = LinkedList()
        self.test_items = [1, 2, 3]