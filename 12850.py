import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()
MOD = 1000000007


N = 8
m = {}
D = int(input())

m[1] = [
    [0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0],
]


def f(d, frm, to):
    if d <= 1:
        return m[d][frm][to]

    m.setdefault(d, [[0 for _ in range(N)] for _ in range(N)])
    if m[d][frm][to]:
        return m[d][frm][to]

    half = d // 2
    other = half + 1 if d % 2 else half  # 홀수면 +1
    # half <= other

    for k in range(N):
        m[d][frm][to] += f(half, frm, k) * f(other, k, to)
        m[d][frm][to] %= MOD

    return m[d][frm][to]


print(f(D, 0, 0))
