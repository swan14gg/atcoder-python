H, W = map(int, input().split())
C = []
for _ in range(H):
    C.append(input())

F = [[0 for _ in range(W + 1)] for _ in range(H + 1)]

for i in range(H - 1, -1, -1):
    for j in range(W - 1, -1, -1):
        if C[i][j] == "#":
            continue
        F[i][j] = max(F[i + 1][j], F[i][j + 1]) + 1

print(F[0][0])
