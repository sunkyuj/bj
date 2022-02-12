import sys
from collections import deque

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

rd_idx = lambda y, x: (2 * n - 1) // 2 + (x - y)
in_range = lambda y, x: 0 <= y < n and 0 <= x < n


n = int(input())
diag = 2 * n - 1

board = [[] for _ in range(n)]
for i in range(n):
    board[i] = list(map(int, input().split()))

ru = [0 for _ in range(diag)]  # 합이 일정
# (0,0) -> ru[0] , (3,4) -> ru[7], (y,x) -> ru[y+x], 왼쪽 위가 0, 오른쪽 아래가 끝
# rd = [0 for _ in range(2 * n - 1)]  # 중앙 기준으로 쁠마
rd = [0 for _ in range(1 << diag)]
# (y,x) -> rd[(2*n-1)//2 + (x-y)], 왼쪽 아래가 0, 오른쪽 위가 끝
bt = [[0 for _ in range()] for _ in range(n)]

ans = 0

for d in range(diag):
    for y in range(d + 1):
        x = d - y
    pass

"""def f(diag, cnt):
    global ans
    if diag == 2 * n:
        ans = max(ans, cnt)
        return

    for y in range(diag + 1):
        x = diag - y
        if in_range(y, x) and board[y][x] == 1 and rd[rd_idx(y, x)] == 0:
            rd[rd_idx(y, x)] = 1
            f(diag + 1, cnt + 1)
            rd[rd_idx(y, x)] = 0

    f(diag + 1, cnt)  # 이번 대각선에서 선택 x"""


# f(0, 0)
print(ans)

"""
20! 나와버림...

10
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1

2 9
3 25
4 81
5 2837
6 2099
7 16728
8 142571
9 24083620
10 2000만 예상
"""
