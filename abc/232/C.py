from itertools import permutations

N, M = map(int, input().split())
RA = [[] for _ in range(N + 1)]
RB = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    RA[a].append(b)
    RA[b].append(a)
for _ in range(M):
    c, d = map(int, input().split())
    RB[c].append(d)
    RB[d].append(c)

ans = "No"
for P in permutations(range(1, N + 1), N):
    ng = False
    for i in range(1, N + 1):
        for r in RA[i]:
            if P[r - 1] not in RB[P[i - 1]]:
                ng = True
                break
        if ng:
            break
    if not ng:
        ans = "Yes"
        break

print(ans)
