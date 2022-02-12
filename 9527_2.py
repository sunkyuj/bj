import sys
import math

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()


def sum_f(x):
    if x <= 0:
        return 0

    seung = int(math.log2(x))  # 2**seung <= x <= 2**(seung+1)
    floor_2pow = 2 ** seung  # <= x 인 2의 ?승
    if floor_2pow == x:
        return seung * x // 2 + 1

    diff = x - floor_2pow
    return sum_f(floor_2pow) + diff + sum_f(diff)


# 2**53 < 10**16 < 2**54
# MAX = 10000000000000000
a, b = map(int, input().split())
print(sum_f(b) - sum_f(a - 1))
