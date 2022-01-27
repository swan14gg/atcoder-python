# 深さ優先探索 TLE

from collections import deque

H, W = map(int, input().split())
C = []
for _ in range(H):
    C.append(input())

stack = deque([])
stack.append((1, 0, 0))

ans = 1
while stack:
    S = stack.pop()
    i, j = S[1], S[2]
    if j + 1 < W and C[i][j + 1] == ".":
        ans = max(S[0] + 1, ans)
        stack.append((S[0] + 1, i, j + 1))
    if i + 1 < H and C[i + 1][j] == ".":
        ans = max(S[0] + 1, ans)
        stack.append((S[0] + 1, i + 1, j))

print(ans)
