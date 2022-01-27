N, K = map(int, input().split())
A = list(map(int, input().split()))
M = {0: 1}

S = [0] * N
for i, a in enumerate(A):
    if i == 0:
        S[i] = a
        continue
    S[i] = S[i - 1] + a

ans = 0
for s in S:
    d = s - K
    if d in M:
        ans += M[d]
    if s in M:
        M[s] += 1
    else:
        M[s] = 1

print(ans)
