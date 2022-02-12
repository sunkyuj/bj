import math
import sys

# from asdf import long

sys.setrecursionlimit(10 ** 8)  # pypy 제출시 삭제!
input = lambda: sys.stdin.readline().rstrip()
# in_range = lambda y,x: 0<=y<n and 0<=x<m

n, m, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]
# arr = list(map(int, long.split()))

b = math.ceil(math.log2(n)) + 1
node_n = 1 << b
seg = [0 for _ in range(node_n)]
seg_add = [0 for _ in range(node_n)]


def make_seg(idx, s, e):
    if s == e:
        seg[idx] = arr[s]
        return seg[idx]

    mid = (s + e) // 2

    l = make_seg(idx * 2, s, mid)
    r = make_seg(idx * 2 + 1, mid + 1, e)
    seg[idx] = l + r

    return seg[idx]


def change(idx, s, e):
    # 탐색 영역 : s~e

    mid = (s + e) // 2
    length = e - s + 1
    seg[idx] += seg_add[idx]
    if idx * 2 < node_n:
        llength, rlength = length // 2 + length % 2, length // 2
        seg_add[idx * 2] += seg_add[idx] // length * llength
        seg_add[idx * 2 + 1] += seg_add[idx] // length * rlength
    seg_add[idx] = 0

    if to < s or e < frm:  # 범위 밖
        return seg[idx]

    if frm <= s and e <= to:  # 탐색 영역이 b~c 완전히 안에 있음
        length = e - s + 1
        seg[idx] += length * d
        if idx * 2 < node_n:
            llength, rlength = length // 2 + length % 2, length // 2
            seg_add[idx * 2] += d * llength
            seg_add[idx * 2 + 1] += d * rlength

        return seg[idx]

    else:  # 탐색 영역이 더 큰 경우나 범위 걸친 경우
        l = change(idx * 2, s, mid)
        r = change(idx * 2 + 1, mid + 1, e)
        seg[idx] = l + r
        return seg[idx]

    """if s == e:
        seg[idx] += d
        return seg[idx]

    mid = (s + e) // 2
    l = change(idx * 2, s, mid)
    r = change(idx * 2 + 1, mid + 1, e)
    seg[idx] = l + r
    return seg[idx]"""


def get(idx, s, e):
    # 탐색 영역 : s~e

    mid = (s + e) // 2
    length = e - s + 1
    seg[idx] += seg_add[idx]
    if idx * 2 < node_n:
        llength, rlength = length // 2 + length % 2, length // 2
        seg_add[idx * 2] += seg_add[idx] // length * llength
        seg_add[idx * 2 + 1] += seg_add[idx] // length * rlength
    seg_add[idx] = 0

    if to < s or e < frm:  # 범위 밖
        return 0

    if frm <= s and e <= to:  # 탐색 영역이 b~c 완전히 안에 있음
        return seg[idx]

    else:  # 탐색 영역이 더 큰 경우나 범위 걸친 경우
        l = get(idx * 2, s, mid)
        r = get(idx * 2 + 1, mid + 1, e)
        return l + r


make_seg(1, 0, len(arr) - 1)


for _ in range(m + k):
    inp = tuple(map(int, input().split()))
    if inp[0] == 1:
        a, b, c, d = inp
        frm, to = b - 1, c - 1
        change(1, 0, len(arr) - 1)
    else:
        a, b, c = inp
        frm, to = b - 1, c - 1
        print(get(1, 0, len(arr) - 1))

    """
5 3 2
1
2
3
4
5
1 3 4 6
2 2 5
1 1 3 -2
1 2 3 -1
2 2 5
    """