from collections import deque

N = int(input())
A = []
stack = deque()
for _ in range(2 * N - 1):
    A.append(list(map(int, input().split())))
used = [False] * (2 * N)


def calc():
    if len(stack) == N:
        ret = 0
        for s in stack:
            ret ^= A[s[0]][s[1] - s[0] - 1]
        return ret
    for i in range(2 * N):
        if not used[i]:
            l = i
            break
    used[l] = True

    ret = 0
    for i in range(2 * N):
        if not used[i]:
            stack.append((l, i))
            used[i] = True
            ret = max(ret, calc())
            stack.pop()
            used[i] = False
    used[l] = False
    return ret


print(calc())
