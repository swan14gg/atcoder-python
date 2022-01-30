N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

s_1 = max(1 - A, 1 - B)
l_1 = min(N - A, N - B)
s_2 = max(1 - A, B - N)
l_2 = min(N - A, B - 1)

for i in range(P, Q + 1):
    m = ""
    for j in range(R, S + 1):
        p_1 = i - j == A - B
        p_2 = i + j == A + B
        if not p_1 and not p_2:
            m += "."
            continue
        k = i - A
        if p_1:
            if s_1 <= k <= l_1:
                m += "#"
                continue
        if p_2:
            if s_2 <= k <= l_2:
                m += "#"
                continue
        m += "."
    print(m)
