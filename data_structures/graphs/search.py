"""Module with implementation of graph traversals."""


from .implementation import Dict, Graph, Location, SimpleGraph
from .queues import Queue


def breadth_first_search(graph: Graph, start: Location):
    """Performs a breadth-first search on a graph
    starting from a specific node.

    Args:
        graph (Graph): The graph to be traversed.
        start (Location): The location where the traversal begins.
    """
    frontier = Queue()
    frontier.put(start)
    reached: Dict[Location, bool] = {start: True}
    while not frontier.empty():
        current: Location = frontier.get()
        print(f"Visiting {current}")
        for node in graph.neighbors(current):
            if node not in reached:
                frontier.put(node)
                reached[node] = True


if __name__ == "__main__":
    example_graph = SimpleGraph()
    example_graph.edges = {
        "A": ["B"],
        "B": ["C"],
        "C": ["B", "D", "F"],
        "D": ["C", "E"],
        "E": ["F"],
        "F": [],
    }

    breadth_first_search(example_graph, "A")
