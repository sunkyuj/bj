import sys
from collections import deque

sys.setrecursionlimit(10 ** 8)  # pypy 제출시 삭제!
input = lambda: sys.stdin.readline().rstrip()
in_range = lambda y, x: 0 <= y < r and 0 <= x < c

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def find(v):
    if v == root[v[0]][v[1]]:
        return v
    root[v[0]][v[1]] = find(root[v[0]][v[1]])
    return root[v[0]][v[1]]


def union(v1, v2):
    r1 = find(v1)
    r2 = find(v2)

    if rank[r1[0]][r1[1]] > rank[r2[0]][r2[1]]:
        root[r2[0]][r2[1]] = r1
    elif rank[r1[0]][r1[1]] < rank[r2[0]][r2[1]]:
        root[r1[0]][r1[1]] = r2
    else:
        root[r2[0]][r2[1]] = r1
        rank[r1[0]][r1[1]] += 1


r, c = map(int, input().split())

board = [list(input()) for _ in range(r)]
root = [[(i, j) for j in range(c)] for i in range(r)]
rank = [[0 for j in range(c)] for i in range(r)]
visit = [[0 for _ in range(c)] for _ in range(r)]
swan = []  # swan[0] = (y1,x1), swan[1] = (y2,x2)

for i in range(r):
    for j in range(c):
        if board[i][j] == "L":
            swan.append((i, j))
            board[i][j] = "."
            if len(swan) == 2:
                break

melt = deque()
for i in range(r):
    for j in range(c):
        if not visit[i][j] and board[i][j] == ".":
            q = deque()
            q.append((i, j))
            visit[i][j] = 1
            while q:
                y, x = q.popleft()
                root[y][x] = (i, j)
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if in_range(ny, nx) and not visit[ny][nx] and board[ny][nx] == ".":
                        visit[ny][nx] = 1
                        q.append((ny, nx))
                    elif (
                        in_range(ny, nx) and not visit[ny][nx] and board[ny][nx] == "X"
                    ):
                        visit[ny][nx] = 1
                        melt.append((ny, nx))
day = 0
while find(swan[0]) != find(swan[1]):
    tmp = deque()
    while melt:
        y, x = melt.popleft()
        board[y][x] = "."
        merge_point = []
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if in_range(ny, nx) and not visit[ny][nx] and board[ny][nx] == "X":
                visit[ny][nx] = 1
                tmp.append((ny, nx))
            elif in_range(ny, nx) and board[ny][nx] == ".":
                merge_point.append((ny, nx))

        for rt in merge_point:
            if find(rt) != find((y, x)):
                union(rt, (y, x))

    melt = tmp
    day += 1
print(day)
