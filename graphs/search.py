from implementation import Graph, SimpleGraph, Location
from queues import Queue


def breadth_first_search(graph: Graph, start: Location):
    frontier = Queue()
    frontier.put(start)
    reached: Dict[Location, bool] = {}
    reached[start] = True

    while not frontier.empty():
        current: Location = frontier.get()
        print("Visiting {0}".format(current))
        for next in graph.neighbors(current):
            if next not in reached:
                frontier.put(next)
                reached[next] = True


if __name__ == '__main__':
    example_graph = SimpleGraph()
    example_graph.edges = {
        'A': ['B'],
        'B': ['C'],
        'C': ['B', 'D', 'F'],
        'D': ['C', 'E'],
        'E': ['F'],
        'F': [],
    }

    breadth_first_search(example_graph, 'A')
