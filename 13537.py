import math
import sys

# sys.setrecursionlimit(10 ** 8)  # pypy 제출시 삭제!
input = lambda: sys.stdin.readline().rstrip()
# in_range = lambda y,x: 0<=y<n and 0<=x<m


n = int(input())
arr = [0] + list(map(int, input().split()))

s = [0 for _ in range(n + 1)]  # 누적합
for i in range(1, n + 1):
    s[i] = s[i - 1] + arr[i]

b = math.ceil(math.log2(n)) + 1
seg = [0 for _ in range(2 ** b)]  # 세그먼트 트리


def make_seg(idx, start, end):

    if idx >= 2 ** b or start > end:
        return
    if start == end:
        seg[idx] = arr[start]
        return
    sec_sum = s[end] - s[start - 1]
    seg[idx] = sec_sum
    mid = (start + end) // 2
 
    make_seg(idx * 2, start, mid)
    make_seg(idx * 2 + 1, mid + 1, end)


make_seg(1, 1, n)


def f(idx, start, end):
    if seg[idx] <= k:
        return 0
    


# print(arr)
m = int(input())
for i in range(m):
    i, j, k = map(int, input().split())

    """sub = arr[i : j + 1]  # O(k) 복잡도라 시간초과
    sub.sort()

    ub_idx = upper_bound(0, len(sub) - 1, k)
    print(len(sub) - ub_idx)
    
    
    

def upper_bound(l, r, k):
    while l <= r:
        mid = (l + r) // 2
        if sub[mid] <= k:
            l = mid + 1
        else:
            r = mid - 1
    return l
"""
