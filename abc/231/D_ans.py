class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def is_same(self, x, y):
        return self.find(x) == self.find(y)


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
