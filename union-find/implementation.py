class QuickFind():
    """An alternative to solve the dynamic connectivity problem.

    connected(): O(1)
    union(): O(n)
    """

    def __init__(self, n):
        self.id = [i for i in range(n)]

    def connected(self, a, b):
        return self.id[a] == self.id[b]

    def union(self, a, b):
        root_a = self.id[a]
        root_b = self.id[b]

        for i in range(len(self.id)):
            if self.id[i] == root_a:
                self.id[i] = root_b


class QuickUnion():
    """An alternative to solve the dynamic connectivity problem.

    root(): O(n)
    connected(): O(n)
    union(): O(n)
    """

    def __init__(self, n):
        self.id = [i for i in range(n)]

    def root(self, x):
        while x != self.id[x]:
            x = self.id[x]
        return x

    def connected(self, a, b):
        return self.root(a) == self.root(b)

    def union(self, a, b):
        root_a = self.root(a)
        root_b = self.root(b)
        self.id[root_a] = root_b


class WeightedQuickUnion():
    """An alternative to solve the dynamic connectivity problem.

    root(): O(log n)
    connected(): O(log n)
    union(): O(log n)
    """

    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.size = [1] * n

    def root(self, x):
        while x != self.id[x]:
            x = self.id[x]
        return x

    def connected(self, a, b):
        return self.root(a) == self.root(b)

    def union(self, a, b):
        root_a = self.root(a)
        root_b = self.root(b)
        if root_a == root_b:
            return

        if self.size[root_a] > self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.size[root_b] += self.size[root_a]
        self.id[root_a] = root_b
