import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()


def fish(j):
    for i in range(R):
        if board[i][j]:
            x = board[i][j][2]
            board[i][j] = 0
            return x
    return 0


def move():
    global board  # board[i][j] 안에는 (s,d,z)의 값이 들어있음. 상어가 없는 경우엔 0이 들어있음
    new_board = [[0 for _ in range(C)] for _ in range(R)]  # 상어들의 새 위치를 담을 공간
    for i in range(R):
        for j in range(C):
            if board[i][j]:
                # 이 상어의 다음 위치는
                ni, nj, nd = get_next_loc(i, j, board[i][j][0], board[i][j][1])
                if new_board[ni][nj]:
                    new_board[ni][nj] = max(
                        new_board[ni][nj],
                        (board[i][j][0], nd, board[i][j][2]),
                        key=lambda x: x[2],
                    )
                else:
                    new_board[ni][nj] = (board[i][j][0], nd, board[i][j][2])

    board = new_board  # board가 이제 상어들의 새 위치를 가리키도록


def get_next_loc(i, j, speed, dir):

    if dir == UP or dir == DOWN:  # i
        cycle = R * 2 - 2
        if dir == UP:
            speed += 2 * (R - 1) - i
        else:
            speed += i

        speed %= cycle
        if speed >= R:
            return (2 * R - 2 - speed, j, UP)
        return (speed, j, DOWN)

    else:  # j
        cycle = C * 2 - 2
        if dir == LEFT:
            speed += 2 * (C - 1) - j
        else:
            speed += j

        speed %= cycle
        if speed >= C:
            return (i, 2 * C - 2 - speed, LEFT)
        return (i, speed, RIGHT)


UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4
R, C, M = map(int, input().split())
board = [[0 for _ in range(C)] for _ in range(R)]

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    r, c = r - 1, c - 1
    board[r][c] = (s, d, z)
    # s : speed
    # d : 1(up), 2(down), 3(right), 4(left)
    # z : size


ans = 0
for j in range(C):
    ans += fish(j)
    move()

print(ans)
