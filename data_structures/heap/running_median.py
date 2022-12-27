"""Implementation of running median algorithm"""

from .implementation import Heap


def rebalance(heap1, heap2):
    element = heap1.pop()
    heap2.insert(element)


def runningMedian(a):
    min_heap = Heap(lambda x, y: x < y)
    max_heap = Heap(lambda x, y: x > y)
    result = []
    for e in a:
        if min_heap.size > 0 and e < min_heap.peek():
            max_heap.insert(e)
            if max_heap.size > min_heap.size + 1:
                rebalance(max_heap, min_heap)
        else:
            min_heap.insert(e)
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

    result = runningMedian(a)

    print("\n".join(map(str, result)))
    print("\n")
