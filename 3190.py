import sys
import queue


sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()


def in_range(nxt):
    return nxt[0] >= 0 and nxt[1] >= 0 and nxt[0] < n and nxt[1] < n


def Input():
    global n, board, k, l, cmd
    n = int(input())
    board = [[0 for j in range(n)] for i in range(n)]
    k = int(input())

    for _ in range(k):
        i, j = map(int, input().split())
        board[i - 1][j - 1] = 2

    l = int(input())
    cmd = []
    for _ in range(l):
        sec, turn = map(str, input().split())
        sec = int(sec)
        cmd.append((sec, turn))
    # print(apple_loc, cmd)


def solution():
    # rdlu, L -> -1, D -> +1
    q = queue.Queue()
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    to = 0
    size = 1
    t = 0
    head, tail = [0, 0], [0, 0]
    board[0][0] = 1
    while True:
        t += 1
        head = [head[0] + move[to][0], head[1] + move[to][1]]
        if not in_range(head) or board[head[0]][head[1]] == 1:
            break
        if board[head[0]][head[1]] == 2:
            q.put(head)
            board[head[0]][head[1]] = 1
            size += 1
        else:
            q.put(head)
            board[head[0]][head[1]] = 1
            board[tail[0]][tail[1]] = 0
            tail = q.get()
        if cmd and t == cmd[0][0]:
            if cmd[0][1] == "L":
                to = (to - 1) % 4
            else:
                to = (to + 1) % 4
            cmd.pop(0)

    print(t)


if __name__ == "__main__":

    Input()
    solution()
