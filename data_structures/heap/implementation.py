"""Implementation of the Heap data structure."""


class Heap:
    """
    Class implementation of the heap data structure

    Parameters
    ----------
    heap_func : function
        Function to be use to keep the heap's invariants.
    """

    def __init__(self, heap_func):
        self._heap = []
        self.size = 0
        self._func = heap_func

    def heapify_down(self, parent):
        """
        Applies the heapify down algorithm to the heap to keep all the invariants.

        Parameters
        ----------
        parent : int
            Index of the node where the heapify down algorithm should start.
        """
        left, right = 2 * parent + 1, 2 * parent + 2
        current = parent
        if left < self.size and self._func(self._heap[left], self._heap[current]):
            current = left
        if right < self.size and self._func(self._heap[right], self._heap[current]):
            current = right
        if current != parent:
            self._heap[parent], self._heap[current] = (
                self._heap[current],
                self._heap[parent],
            )
            self.heapify_down(current)

    def heapify_up(self, child):
        """
        Applies the heapify up algorithm to the heap to keep all the invariants.

        Parameters
        ----------
        child : int
            Index of the node where the heapify up algorithm should start.
        """
        parent, current = (child - 1) // 2, child
        while parent >= 0:
            if self._func(self._heap[current], self._heap[parent]):
                self._heap[current], self._heap[parent] = (
                    self._heap[parent],
                    self._heap[current],
                )
            parent, current = (parent - 1) // 2, parent

    def insert(self, element):
        """
        Inserts an element to the heap and keeps the heap's invariants after it.

        Parameters
        ----------
        element
            Element to be inserted in the heap.
        """
        self._heap.append(element)
        self.size += 1
        self.heapify_up(self.size - 1)

    def peek(self):
        """Returns the element in the root of the heap without removing it."""
        return self._heap[0] if self.size > 0 else None

    def pop(self):
        """Returns the element in the root of the heap removing it
        and keeping heap's invariants after it.
        """
        root = self.peek()
        self._heap[0] = self._heap[self.size - 1]
        self.size -= 1
        self._heap.pop()
        if self.size > 0:
            self.heapify_down(0)
        return root

    @property
    def heap(self):
        """Property to have access to the heap internal structure."""
        return self._heap
