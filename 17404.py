import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
rgb = [0 for _ in range(n)]

for i in range(n):
    r, g, b = map(int, input().split())
    rgb[i] = [r, g, b]

dp = [[[999999, 999999, 999999] for _ in range(n)] for _ in range(3)]


for root in range(3):
    dp[root][0][root] = rgb[0][root]
    for i in range(1, n):
        for x in range(3):
            if i == n - 1 and root == x:
                continue
            dp[root][i][x] = (
                min(dp[root][i - 1][(x + 1) % 3], dp[root][i - 1][(x + 2) % 3])
                + rgb[i][x]
            )

m = 99999999
for root in range(3):
    for x in range(3):
        m = min(m, dp[root][n - 1][x])
print(m)
