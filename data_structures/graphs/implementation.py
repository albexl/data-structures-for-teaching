from typing import Dict, Iterator, List, Protocol, TypeVar, Tuple

Location = TypeVar('Location')


class Graph(Protocol):
    def neighbors(self, id: Location) -> List[Location]:
        pass


class SimpleGraph:

    def __init__(self):
        self.edges: Dict[Location, List[Location]] = {}

    def neighbors(self, id: Location) -> List[Location]:
        return self.edges[id]


GridLocation = Tuple[int, int]


class Grid:
    def __init__(height: int, width: int):
        self.height = height
        self.width = width
        self.walls: List[GridLocation] = []

    def in_bounds(self, id: GridLocation) -> bool:
        (x, y) = id
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    def passable(self, id: GridLocation):
        return id not in self.walls

    def neighbors(self, id: GridLocation) -> Iterator[GridLocation]:
        (x, y) = id
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        neighbors = [(x + dx[i], y + dy[i]) for i in range(len(dx))]
        neighbors = filter(self.in_bounds, neighbors)
        neighbors = filter(self.passable, neighbors)
        return neighbors
