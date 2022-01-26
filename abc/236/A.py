S = input()
a, b = map(int, input().split())
I = list(range(len(S)))
I[a - 1] = b - 1
I[b - 1] = a - 1
ans = ""
for i in I:
    ans += S[i]
print(ans)
