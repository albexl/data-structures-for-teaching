from implementation import Graph, Location
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
