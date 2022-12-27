class Heap:
    def __init__(self, heap_func):
        self._heap = []
        self.size = 0
        self._func = heap_func

    def heapify_down(self, parent):
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
        parent, current = (child - 1) // 2, child
        while parent >= 0:
            if self._func(self._heap[current], self._heap[parent]):
                self._heap[current], self._heap[parent] = (
                    self._heap[parent],
                    self._heap[current],
                )
            parent, current = (parent - 1) // 2, parent

    def insert(self, element):
        self._heap.append(element)
        self.size += 1
        self.heapify_up(self.size - 1)

    def peek(self):
        return self._heap[0] if self.size > 0 else None

    def pop(self):
        root = self.peek()
        self._heap[0] = self._heap[self.size - 1]
        self.size -= 1
        self._heap.pop()
        if self.size > 0:
            self.heapify_down(0)
        return root

    @property
    def heap(self):
        return self._heap
