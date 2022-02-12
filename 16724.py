import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()


def union(nxt: tuple, cur: tuple):
    nxt_root = find(nxt[0], nxt[1])
    cur_root = find(cur[0], cur[1])
    root[cur_root[0]][cur_root[1]] = nxt_root


def find(i, j):
    if (i, j) == root[i][j]:
        return (i, j)
    root[i][j] = find(root[i][j][0], root[i][j][1])
    return root[i][j]


def dfs(y, x):
    visit[y][x] = 1
    ny, nx = y, x
    if board[y][x] == "U":
        ny -= 1
    elif board[y][x] == "D":
        ny += 1
    elif board[y][x] == "L":
        nx -= 1
    elif board[y][x] == "R":
        nx += 1

    next_root = find(ny, nx)
    if next_root == (ny, nx) and board[ny][nx] != "S":  # not a cycle
        union((ny, nx), (y, x))
        dfs(ny, nx)

    else:  # next location is a cycle
        if next_root == (y, x):  # 새 사이클 형성
            board[y][x] = "S"
            global ans
            ans += 1
            return
        else:  # 기존 사이클에 들어가는 경우
            union((ny, nx), (y, x))
            return


n, m = map(int, input().split())
board = [[] for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]
root = [[(i, j) for j in range(m)] for i in range(n)]
for i in range(n):
    board[i] = list(input())

ans = 0
for i in range(n):
    for j in range(m):
        if visit[i][j]:
            continue
        dfs(i, j)
print(ans)
