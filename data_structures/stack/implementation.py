"""Stack implementations."""


class LinkedStack():
    """Implementation of stack using linked list."""

    def __init__(self):
        self.first = None

    def is_empty(self) -> bool:
        """Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.first is None

    def push(self, item):
        """Inserts the supplied item to the top of the stack.

        Args:
            item (any): The item to be inserted.
        """
        old_first = self.first
        self.first = (item, old_first)

    def pop(self):
        """Returns the item at the top of the stack.

        Returns:
            any: The item at the top of the stack.
        """
        item = self.first[0]
        self.first = self.first[1]
        return item


class ArrayBasedStack():
    """Implementation of stack using array."""

    def __init__(self):
        self.container = [None]
        self.size = 0

    def is_empty(self):
        """Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.size == 0

    def push(self, item):
        """Inserts the supplied item to the top of the stack.

        Args:
            item (any): The item to be inserted.
        """
        if self.size == len(self.container):
            self._resize(2 * len(self.container))
        self.container[self.size] = item
        self.size += 1

    def pop(self):
        """Returns the item at the top of the stack.

        Returns:
            any: The item at the top of the stack.
        """
        self.size -= 1
        item = self.container[self.size]
        self.container[self.size] = None
        if self.size > 0 and self.size == len(self.container // 4):
            self._resize(len(self.container) // 2)
        return item

    def _resize(self, capacity):
        copy = [None] * capacity
        for i in range(self.size):
            copy[i] = self.container[i]
        self.container = copy
