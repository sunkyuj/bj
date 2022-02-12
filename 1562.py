import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

MOD = 1000000000

n = int(input())

dp = [[0 for inc in range(1024)] for i in range(10)]

for x in range(1, 10):
    dp[x][1 << x] = 1

for l in range(2, n + 1):
    dp_next = [[0 for inc in range(1024)] for i in range(10)]
    for last in range(10):
        for inc in range(1024):
            if last < 9:
                dp_next[last][inc | (1 << last)] = (
                    dp_next[last][inc | (1 << last)] + dp[last + 1][inc]
                )
            if last > 0:
                dp_next[last][inc | (1 << last)] = (
                    dp_next[last][inc | (1 << last)] + dp[last - 1][inc]
                )
    dp = dp_next

print(sum([dp[i][1023] for i in range(10)]))


# print(cnt % MOD)
