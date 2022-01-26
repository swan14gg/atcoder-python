N, K = map(int, input().split())
P = list(map(int, input().split()))

A = [False] * (N + 1)

for p in P[:K]:
    A[p] = True


def search(i):
    i += 1
    while not A[i]:
        i += 1
    return i


i = search(0)
print(i)

for p in P[K:]:
    if i < p:
        A[p] = True
        i = search(i)
        print(i)
    else:
        print(i)
