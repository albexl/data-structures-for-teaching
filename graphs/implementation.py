from typing import Dict, List, Protocol, TypeVar


Location = TypeVar('Location')


class Graph(Protocol):
    def neighbors(self, id: Location) -> List[Location]:
        pass


class SimpleGraph:

    def __init__(self):
        self.edges: Dict[Location, List[Location]] = {}

    def neighbors(self, id: Location) -> List[Location]:
        return self.edges[id]
