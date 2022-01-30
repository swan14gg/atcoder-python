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


N, M = map(int, input().split())
uf = UnionFind(N)
C = [0] * N
is_same = False
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if uf.is_same(a, b):
        is_same = True
        break
    uf.unite(a, b)
    C[a] += 1
    C[b] += 1

if max(C) <= 2 and not is_same:
    print("Yes")
else:
    print("No")
