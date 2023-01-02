"""Implementation of running median algorithm"""


from typing import List

from .implementation import Heap


def rebalance(heap1: Heap, heap2: Heap):
    """Adds the root element of `heap1` to `heap2`.

    Args:
        heap1 (Heap): Heap to remove the root element.
        heap2 (Heap): Heap to add a new element.
    """
    element = heap1.pop()
    heap2.insert(element)


def running_median(items: List[int]):
    """Returns a list with the median element for
    every prefix of the list `items`.

    Args:
        items (List[int]): List of integers to find the running median.

    Returns:
        List[int]: A list containing the median element for every prefix of `items`.
    """
    min_heap = Heap(lambda x, y: x < y)
    max_heap = Heap(lambda x, y: x > y)
    result = []
    for elem in items:
        if min_heap.size > 0 and elem < min_heap.peek():
            max_heap.insert(elem)
            if max_heap.size > min_heap.size + 1:
                rebalance(max_heap, min_heap)
        else:
            min_heap.insert(elem)
            if min_heap.size > max_heap.size + 1:
                rebalance(min_heap, max_heap)

        if min_heap.size == max_heap.size:
            median = (min_heap.peek() + max_heap.peek()) / 2
        elif min_heap.size == max_heap.size + 1:
            median = min_heap.peek()
        else:
            median = max_heap.peek()
        result.append(float(median))

    return result


if __name__ == "__main__":
    a_count = int(input().strip())

    a = []
    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    medians = running_median(a)

    print("\n".join(map(str, medians)))
    print("\n")
