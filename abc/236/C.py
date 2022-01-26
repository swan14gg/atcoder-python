N, M = map(int, input().split())
S = input().split()
T = input().split()

iM = 0
for iN in range(N):
    if S[iN] == T[iM]:
        print("Yes")
        iM += 1
    else:
        print("No")
