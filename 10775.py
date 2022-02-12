import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()


G = int(input())
P = int(input())

p_info = [0 for _ in range(P + 1)]
gate_cnt = [0 for _ in range(G + 1)]

for i in range(1, P + 1):
    p_info[i] = int(input())


def f():
    for i in range(1, P + 1):
        cur = p_info[i]
        while cur > 0 and gate_cnt[cur]:
            move = gate_cnt[cur]
            gate_cnt[cur] += 1
            cur -= move

        if cur == 0:
            return i - 1
        gate_cnt[cur] += 1
    return i


print(f())
