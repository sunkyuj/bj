from itertools import permutations
import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
innings = [list(map(int, input().split())) for _ in range(n)]
M = 0


def f(order):
    score = 0
    idx = 0
    for inning in innings:
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            if inning[order[idx]] == 0:
                out += 1
            elif inning[order[idx]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif inning[order[idx]] == 2:
                score += b3 + b2
                b1, b2, b3 = 0, 1, b1
            elif inning[order[idx]] == 3:
                score += b3 + b2 + b1
                b1, b2, b3 = 0, 0, 1
            else:
                score += b3 + b2 + b1 + 1
                b1, b2, b3 = 0, 0, 0

            idx = (idx + 1) % 9

    return score


for P in permutations([1, 2, 3, 4, 5, 6, 7, 8], 8):
    order = list(P[:3]) + [0] + list(P[3:])
    M = max(M, f(order))

print(M)
