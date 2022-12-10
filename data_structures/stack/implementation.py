class LinkedStack():

    def __init__(self):
        self.first = None

    def is_empty(self):
        return self.first is None

    def push(self, item):
        old_first = self.first
        self.first = (item, old_first)

    def pop(self):
        item = self.first[0]
        self.first = self.first[1]
        return item


class ArrayBasedStack():

    def __init__(self):
        self.container = [None]
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def pop(self):
        self.size -= 1
        item = self.container[self.size]
        self.container[self.size] = None
        if self.size > 0 and self.size == len(self.container // 4):
            self._resize(len(self.container) // 2)
        return item

    def push(self, item):
        if self.size == len(self.container):
            self._resize(2 * len(self.container))
        self.container[self.size] = item
        self.size += 1

    def _resize(self, capacity):
        copy = [None] * capacity
        for i in range(self.size):
            copy[i] = self.container[i]
        self.container = copy
