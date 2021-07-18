import collections
from implementation import Location


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self) -> bool:
        return not self.elements

    def put(self, x: Location):
        self.elements.append(x)

    def get(self) -> Location:
        return self.elements.popleft()
