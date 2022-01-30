N, M = map(int, input().split())
S = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    S[a].append(b)
    S[b].append(a)

ans = "Yes"
for s in S:
    length = len(s)
    if length > 2:
        ans = "No"
        break
    if length == 0 or length == 1:
        continue
    a, b = s[0], s[1]
    if b in S[a] or a in S[b]:
        ans = "No"
        break

print(ans)
