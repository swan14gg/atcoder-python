N = int(input())
A = list(map(int, input().split()))


def calc_sum(f):
    dp1 = [0] * N  # 引かない
    dp2 = [0] * N  # 引く
    dp2[0] = f(A[0])
    for i in range(1, N):
        dp1[i] = dp2[i - 1]
        dp2[i] = max(dp1[i - 1], dp2[i - 1]) + f(A[i])
    return max(dp1[N - 1], dp2[N - 1])


def binary_search(l, r, f):
    while r - l > 1:
        mid = (r + l) // 2
        if f(mid):
            l = mid
        else:
            r = mid
    return l


MIN = 1
MAX = 10 ** 9 + 1
P = 10 ** 3

f1 = lambda x: calc_sum(lambda y: y * P - x) >= 0
ans1 = binary_search(MIN, MAX * P, f1) / P

f2 = lambda x: calc_sum(lambda y: 1 if y >= x else -1) > 0
ans2 = binary_search(MIN, MAX, f2)

print(ans1)
print(ans2)
