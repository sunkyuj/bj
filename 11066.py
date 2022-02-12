import sys

# sys.setrecursionlimit(10 ** 8) <-- pypy 제출시 주석처리 안 하면 메모리초과...
input = lambda: sys.stdin.readline().rstrip()
MAX = 1000000000

tc = int(input())
for _ in range(tc):
    k = int(input())
    c = list(map(int, input().split()))

    dp = [[MAX for _ in range(k)] for _ in range(k)]

    s = [0 for _ in range(k + 1)]  # 누적합
    for i in range(k):
        s[i] = s[i - 1] + c[i]

    for i in range(k):  # 길이 0
        dp[i][i] = 0

    for l in range(1, k):  # 길이 1 ~ k-1
        for i in range(k - l):
            j = i + l  # 끝점 j
            total = s[j] - s[i - 1]  # 구간합
            for m in range(i, j):  # i~j 사이 임의의 m에 대해
                dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j] + total)  # 최소를 찾는 것

    print(dp[0][k - 1])
