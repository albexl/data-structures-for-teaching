"""Module to store the implementation of queues in order to make different traversals on graphs."""


import collections

from .implementation import Location


class Queue:
    """implementation of a queue."""

    def __init__(self):
        self.elements = collections.deque()

    def empty(self) -> bool:
        """Checks if the queue is empty or not.

        Returns:
            bool: True if the queue has no elements, False otherwise.
        """
        return not self.elements

    def put(self, node: Location):
        """Appends a node to the end of the queue.

        Args:
            node (Location): The node to be appended.
        """
        self.elements.append(node)

    def get(self) -> Location:
        """Returns the leftmost node of the queue.

        Returns:
            Location: The retrieved node/
        """
        return self.elements.popleft()
