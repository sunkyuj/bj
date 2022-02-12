import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

MAX = 400000


def get_add(lr, k):  # 어떤 발이 k->lr 발로 갈 때 드는 비용
    if k == 0:
        if lr == 0:
            return 0
        else:
            return 2
    elif k == lr:
        return 1
    elif abs(k - lr) == 1 or abs(k - lr) == 3:
        return 3
    else:
        return 4


move = list(map(int, input().split()))
move.pop()
n = len(move)
if n == 0:
    print(0)
    exit()

dp = [[[MAX + 1 for _ in range(5)] for _ in range(5)] for _ in range(n + 1)]
dp[-1][0][0] = 0

for i in range(n):
    # l = move[i], 왼발로 이번 위치 누를 때, 즉 이번에 왼발이 움직일 것
    for r in range(5):  # 왼발이 움직이니 오른발은 고정
        for k in range(5):  # k 는 왼발의 이전 위치.
            add = get_add(move[i], k)  # 왼발이 k에서 move[i]로 움직일 때 드는 비용
            dp[i][move[i]][r] = min(dp[i][move[i]][r], dp[i - 1][k][r] + add)

    # r = move[i], 오른발로 이번 위치 누를 때, 즉 이번에 오른발이 움직일 것
    for l in range(5):  # 오른발이 움직이니 왼발은 고정
        for k in range(5):  # k는 오른발의 이전 위치.
            add = get_add(move[i], k)  # 오른발이 k에서 move[i]로 움직일 때 드는 비용
            dp[i][l][move[i]] = min(dp[i][l][move[i]], dp[i - 1][l][k] + add)

m = MAX + 1
for l in range(5):
    for r in range(5):
        m = min(m, dp[n - 1][l][r])
print(m)
