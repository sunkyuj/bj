import sys
import math

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()


def sum_f(x):
    if x <= 1:
        return x

    seung = math.floor(math.log2(x))  # 2**seung <= x <= 2**(seung+1)
    if 2 ** seung == x:
        return sum_2pow[seung]

    diff = x - 2 ** seung
    return sum_2pow[seung] + diff + sum_f(diff)


# 2**53 < 10**16 < 2**54
MAX = 10000000000000000
a, b = map(int, input().split())

sum_2pow = [0 for _ in range(60)]
sum_2powx_min1 = [0 for _ in range(60)]

sum_2pow[0] = 1  # 2**0 == 1 --> sum f(1) == 1
sum_2pow[1] = 2  # 2**1 == 2 --> sum f(2) == 2
sum_2powx_min1[1] = 1  # 2**1 - 1 == 1 --> sum f(1) == 1z

for i in range(2, 60):
    sum_2powx_min1[i] = sum_2powx_min1[i - 1] * 2 + (2 ** i) // 2
    sum_2pow[i] = sum_2powx_min1[i] + 1

print(sum_f(b) - sum_f(a - 1))
