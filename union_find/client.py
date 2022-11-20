"""Client code to test the Union Find implementations."""

from .implementation import QuickFind

if __name__ == '__main__':
    n = int(input())
    union_find = QuickFind(n)

    m = int(input())
    for _ in range(m):
        a, b = int(input()), int(input())

        if not union_find.connected(a, b):
            union_find.union(a, b)
            print(a, b)
