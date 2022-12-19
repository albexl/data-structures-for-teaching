"""Module with different implementations of graphs."""


from typing import Dict, Iterator, List, Protocol, Tuple, TypeVar

Location = TypeVar("Location")


class Graph(Protocol):
    """The Graph protocol."""

    def neighbors(self, node_id: Location) -> List[Location]:
        """Returns the neighbor locations for a specific location.

        Args:
            node_id (Location): Location to find neighbors.

        Returns:
            List[Location]: Neighbors of the supplied location.
        """


class SimpleGraph(Graph):
    """Implementation of a Simple Graph."""

    def __init__(self):
        self.edges: Dict[Location, List[Location]] = {}

    def neighbors(self, node_id: Location) -> List[Location]:
        return self.edges[node_id]


GridLocation = Tuple[int, int]


class Grid(Graph):
    """Implementation of a Grid Graph."""

    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.walls: List[GridLocation] = []

    def in_bounds(self, node_id: GridLocation) -> bool:
        """Checks if a coordinate is inside the grid.

        Args:
            node_id (GridLocation): The coordinate to check.

        Returns:
            bool: True if the location is in bounds, False otherwise.
        """
        (pos_x, pos_y) = node_id
        return 0 <= pos_x < self.width and 0 <= pos_y < self.height

    def passable(self, node_id: GridLocation) -> bool:
        """Checks if a coordinate can be traversed. This means
        the coordinate is not a wall.

        Args:
            node_id (GridLocation): The coordinate to check.

        Returns:
            bool: True if the location is passable, False otherwise.
        """
        return node_id not in self.walls

    def neighbors(self, node_id: GridLocation) -> Iterator[GridLocation]:
        (pos_x, pos_y) = node_id
        dir_x = [1, -1, 0, 0]
        dir_y = [0, 0, 1, -1]
        neighbors = [(pos_x + dir_x[i], pos_y + dir_y[i]) for i in range(len(dir_x))]
        neighbors = filter(self.in_bounds, neighbors)
        neighbors = filter(self.passable, neighbors)
        return neighbors
