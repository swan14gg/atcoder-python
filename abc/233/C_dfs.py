N, X = map(int, input().split())
A = []
L = []
for _ in range(N):
    l, *a = map(int, input().split())
    L.append(l)
    A.append(a)

ans = 0


def dfs(i, p):
    global ans
    if i == N:
        if p == X:
            ans += 1
        return
    for a in A[i]:
        if a * p > X:
            continue
        dfs(i + 1, p * a)


dfs(0, 1)
print(ans)
