N, X = map(int, input().split())
A = []
L = []
for _ in range(N):
    l, *a = map(int, input().split())
    L.append(l)
    A.append(a)

M = {X: 1}

for a in A:
    new = {}
    for i in a:
        for k, v in M.items():
            s = k % i
            if s != 0:
                continue
            q = k // i
            if q in new:
                new[q] += v
            else:
                new[q] = v
    M = new

if 1 in M:
    ans = M[1]
else:
    ans = 0
print(ans)
