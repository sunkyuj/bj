import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()


def rotate(A, r, c, s):

    B = [[0 for __ in range(2 * s + 1)] for _ in range(2 * s + 1)]
    """for i in range(r - s, r + s + 1):
        for j in range(c - s, c + s + 1):
            B[j][l - 1 - i] = A[i][j]"""
    for layer in range(1, s + 1):
        l = 2 * s + 1
        start = (r - s, c - s)
        to = [r - s, c - s + 1]
        dy, dx = 0, 1

        while to != list(start):
            pass
    for i in B:
        print(i)


def Input():
    global n, m, k
    n, m, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    for _ in range(k):
        r, c, s = map(int, input().split())
        rotate(A, r - 1, c - 1, s)

    # r,c 에 각각 -1 해주자 index다


if __name__ == "__main__":
    Input()
    # Solve()
