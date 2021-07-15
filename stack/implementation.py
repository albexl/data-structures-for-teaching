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
        self.N = 0

    def is_empty(self):
        return self.N == 0

    def pop(self):
        self.N -= 1
        item = self.container[self.N]
        self.container[self.N] = None
        if self.N > 0 and self.N == len(self.container // 4):
            self.resize(len(self.container) // 2)
        return item

    def push(self, item):
        if self.N == len(self.container):
            self.resize(2 * len(self.container))
        self.container[self.N] = item
        self.N += 1

    def resize(self, capacity):
        copy = [None] * capacity
        for i in range(self.N):
            copy[i] = self.container[i]
        self.container = copy
