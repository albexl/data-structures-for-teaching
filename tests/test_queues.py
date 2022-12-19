"""Module to test the Queue implementations."""


from unittest import TestCase

from data_structures.graphs.queues import Queue


class TestQueue(TestCase):
    """Class to test the Queue implementation."""

    def setUp(self):
        self.queue = Queue()
        self.test_items = ["A", "B", "C"]

    def test_empty_queue(self):
        """Checks queue is empty when just created."""
        self.assertTrue(self.queue.empty())

    def test_put_and_get(self):
        """Check the queue returns the elements in the same order they were added."""
        for item in self.test_items:
            self.queue.put(item)
        retrieved_items = []
        while not self.queue.empty():
            retrieved_items.append(self.queue.get())
        self.assertEqual(retrieved_items, self.test_items)
