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
        for i in range(1, self.linked_list.length()+1):
            retrieved_items.append(self.linked_list.get(i))

        self.assertEqual(retrieved_items, self.test_items)

    def test_clear(self):
        """Check the LinkedList delete all elements from LinkedList."""
        for item in self.test_items:
            self.linked_list.add(item)

        #Delete all elements from LinkedList
        self.linked_list.clear()

        #Verify delete
        self.assertEqual(0, self.linked_list.length())
        self.assertTrue(self.linked_list.is_empty())

    def test_insert(self):
        """Check the LinkedList insert a given element in the right place."""
        for item in self.test_items:
            self.linked_list.add(item)  
        
        #Try to insert element 5 in a invalid position (0)
        with self.assertRaises(ValueError) as e:
            self.linked_list.insert(5, 0)
        #Verify the exception message
        self.assertEqual(str(e.exception), 'Index out of range')

        #Try to insert element 5 in another invalid position (-2)
        with self.assertRaises(ValueError) as e:
            self.linked_list.insert(5, -2)
        #Verify the exception message
        self.assertEqual(str(e.exception), 'Index out of range')

        #Insert element 5 in a valid position (2)
        self.linked_list.insert(5, 2)

        #Verify insertion
        retrieved_items = []
        for i in range(1, self.linked_list.length()+1):
            retrieved_items.append(self.linked_list.get(i))
        self.assertEqual(retrieved_items, [1, 5, 2, 3])

    def test_contains(self):
        """Check if the LinkedList contains a given element."""
        for item in self.test_items:
            self.linked_list.add(item)

        #Check the existence of an element (2)
        self.assertTrue(self.linked_list.contains(2))

        #Check no existence of an element (5)
        self.assertFalse(self.linked_list.contains(5))

    def test_remove(self):
        """Check the removal of an element in the LinkedList"""
        for item in self.test_items:
            self.linked_list.add(item)

        #Try to remove element in a invalid position (0)
        with self.assertRaises(ValueError) as e:
            self.linked_list.remove(0)
        #Verify the exception message
        self.assertEqual(str(e.exception), 'Index out of range')

        #Try to remove element in another invalid position (-3)
        with self.assertRaises(ValueError) as e:
            self.linked_list.remove(-3)
        #Verify the exception message
        self.assertEqual(str(e.exception), 'Index out of range')

        #Remove element in a second position (2)
        self.linked_list.remove(2)

        #Verify removal
        retrieved_items = []
        for i in range(1, self.linked_list.length()+1):
            retrieved_items.append(self.linked_list.get(i))
        self.assertEqual(retrieved_items, [1, 3])
    
    def test_copy_to(self):
        """Check the copy element(s) from a given position in LinkedList to another list"""
        for item in self.test_items:
            self.linked_list.add(item)

        aux_list = [4, 5]
        #Try to copy_to from an invalid position
        with self.assertRaises(ValueError) as e:
            self.linked_list.copy_to(aux_list, -1)
        #Verify the exception message
        self.assertEqual(str(e.exception), 'Index out of range')
        
        #Try to copy from another invalid position (100)
        with self.assertRaises(ValueError) as e:
            self.linked_list.copy_to(aux_list, 100)
        #Verify the exception message
        self.assertEqual(str(e.exception), 'Index out of range')
        
        #Verify copy
        self.linked_list.copy_to(aux_list, 2)
        self.assertEqual(aux_list, [4, 5, 2, 3])

class TestLinkedList(BaseTestLinkedList):
    """Class to test the LinkedList implementation."""

    __test__ = True

    def setUp(self):
        self.linked_list = LinkedList()
        self.test_items = [1, 2, 3]