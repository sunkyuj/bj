import sys
from queue import PriorityQueue

# sys.setrecursionlimit(10 ** 8)  # pypy 제출시 삭제!
input = lambda: sys.stdin.readline().rstrip()
in_range = lambda y, x: 0 <= y < h and 0 <= x < w

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def priority(c):
    if c == "$":  # goal
        return 0
    if "a" <= c <= "z":  # key
        return 1
    if c == ".":  # space
        return 3
    if "A" <= c <= "Z":  # door
        if c.lower() in keys:  # 열 수 있는 문
            return 2
        else:  # 못 여는 문
            return 4


for _ in range(int(input())):
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    keys = set(input())

    found_locked_door = {}  # 잠겨있는 문이 있는 위치들
    for alp in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        found_locked_door.setdefault(alp, set())  # 특정 알파벳의 문이 둘 이상일수도 있어서 문 위치를 set에 저장

    visit = [[0 for _ in range(w)] for _ in range(h)]
    pq = PriorityQueue()

    ans = 0
    for i in range(h):
        for j in range(w):
            # 가장자리만 탐색
            if (i == 0 or i == h - 1 or j == 0 or j == w - 1) and board[i][j] != "*":
                p = priority(board[i][j])
                if p == 4:  # 못 여는 문
                    found_locked_door[board[i][j]].add((i, j))
                    continue
                pq.put((p, i, j))
                visit[i][j] = 1

    while not pq.empty():
        p, y, x = pq.get()

        if p == 0:  # goal
            ans += 1
        elif p == 1:  # key
            keys.add(board[y][x])
            if board[y][x].upper() in found_locked_door:  # 해당 열쇠에 맞는 문 찾았었음, 열어버리자!
                for door_y, door_x in found_locked_door[board[y][x].upper()]:
                    # 해당 열쇠에 맞는, 이미 찾았었던, 모든 문에 대해
                    visit[door_y][door_x] = 1
                    pq.put((2, door_y, door_x))
        elif p == 2 or p == 3:
            pass

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if in_range(ny, nx) and not visit[ny][nx] and board[ny][nx] != "*":
                np = priority(board[ny][nx])
                if np == 4:  # 못 여는 문
                    found_locked_door[board[ny][nx]].add((ny, nx))
                    continue
                visit[ny][nx] = 1
                pq.put((np, ny, nx))

    print(ans)
