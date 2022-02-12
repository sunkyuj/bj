import sys
import math

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()


n = int(input())
dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = 1 + dp[i - 1]  # 전에거 + 1 한거를 일단 넣어줌
    for j in range(2, int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], 1 + dp[i - (j ** 2)])  # 제곱수는 무조건 1이므로, 1 + dp[i-(j**2)]

print(dp[n])
