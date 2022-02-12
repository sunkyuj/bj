import math
import sys


# sys.setrecursionlimit(10 ** 8)  # pypy 제출시 삭제!
input = lambda: sys.stdin.readline().rstrip()
# in_range = lambda y,x: 0<=y<n and 0<=x<m
MAX = 1000000000


def make_seg(idx, s, e):
    if s == e:
        seg[idx] = histograms[s]
        return seg[idx]

    # w = e-s+1
    mid = (s + e) // 2
    l = make_seg(idx * 2, s, mid)
    r = make_seg(idx * 2 + 1, mid + 1, e)
    seg[idx] = min(l, r)
    return seg[idx]


def f(frm, to):
    if frm == to:
        return histograms[frm]

    mid = (frm + to) // 2
    l = f(frm, mid)
    r = f(mid + 1, to)

    max_val = max(l, r)

    # including border
    h = min(histograms[mid], histograms[mid + 1])
    w = 2
    s = w * h
    i, j = mid, mid + 1
    while frm < i or j < to:  # i==frm and j==to 가 되면 종료

        if frm != i and to == j:  # 무조건 i 움직임
            i -= 1
            w += 1
            h = min(h, histograms[i])
            s = max(s, w * h)

        elif frm == i and to != j:  # 무조건 j 움직임
            j += 1
            w += 1
            h = min(h, histograms[j])
            s = max(s, w * h)

        elif frm != i and to != j:  # 비교 후 더 큰 쪽으로 움직임
            if histograms[i - 1] >= histograms[j + 1]:
                i -= 1
                w += 1
                h = min(h, histograms[i])
                s = max(s, w * h)
            else:
                j += 1
                w += 1
                h = min(h, histograms[j])
                s = max(s, w * h)

    max_val = max(max_val, s)

    return max_val


while True:
    inp = list(map(int, input().split()))
    n = inp[0]
    if n == 0:
        break
    histograms = inp[1:]

    b = math.ceil(math.log2(n)) + 1
    node_n = 1 << b
    seg = [0] * node_n  # 구간의 min h 를 가짐
    make_seg(1, 0, len(histograms) - 1)

    print(f(0, len(histograms) - 1))

"""
7 7 1 5 9 6 7 3
7 1 4 4 4 4 1 1
4 1 8 2 2
"""
