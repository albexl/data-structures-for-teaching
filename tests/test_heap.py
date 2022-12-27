"""Module to test the Heap implementations."""

from unittest import TestCase

from data_structures.heap.implementation import Heap


class TestHeap(TestCase):
    def setUp(self):
        self.min_heap = Heap(lambda x, y: x < y)
        self.elements = [3, 2, 6, 1, 3]

    def _test_add_elements(self):
        """Util function to add elements to the heap"""
        for element in self.elements:
            self.min_heap.insert(element)
        self.assertEqual(self.min_heap.size, 5)
        self.assertEqual(self.min_heap.heap, [1, 2, 6, 3, 3])
    
    def _test_pop_elements(self):
        """Util function to pop elements from the heap"""
        popped_elements = []
        while self.min_heap.size > 0:
            popped_elements.append(self.min_heap.pop())
        self.assertEqual(self.min_heap.size, 0)
        self.assertEqual(popped_elements, [1, 2, 3, 3, 6])

    def test_empty_heap(self):
        """Check the invariants when the heap is empty"""
        self.assertEqual(self.min_heap.size, 0)
        self.assertEqual(self.min_heap.heap, [])

    def test_insert_pop_elements(self):
        """Check that the elements are popped from the heap in ascending order"""
        self._test_add_elements()
        self._test_pop_elements()

    def test_peek_elements(self):
        """Check the invariants when peeking an element from the heap"""
        self._test_add_elements()
        item = self.min_heap.peek()
        self.assertEqual(self.min_heap.size, 5)
        self.assertEqual(item, 1)
