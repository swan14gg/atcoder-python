class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def root(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.root(self.parents[x])
        return self.parents[x]

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        self.parents[rx] = ry

    def is_same(self, x, y):
        return self.root(x) == self.root(y)


N, Q = map(int, input().split())

uf = UnionFind(N)
for _ in range(Q):
    p, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if p == 0:
        uf.unite(a, b)
    else:
        if uf.is_same(a, b):
            print("Yes")
        else:
            print("No")
