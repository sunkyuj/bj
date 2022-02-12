import sys
import math
from itertools import combinations

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    n = int(input())
    ps = [0 for _ in range(n)]
    xtotal, ytotal = 0, 0
    for i in range(n):
        x, y = map(int, input().split())
        xtotal += x
        ytotal += y
        ps[i] = (x, y)

    min_scala = 1000000
    comb = list(combinations(range(n), n // 2))
    for c in comb[: len(comb) // 2]:  # 조합은 어떨 때 절반만 봐도 됨

        xsum, ysum = 0, 0
        for i in c:
            xsum += ps[i][0]
            ysum += ps[i][1]

        xsum -= xtotal - xsum
        ysum -= ytotal - ysum

        scala = math.sqrt(xsum ** 2 + ysum ** 2)
        if min_scala > scala:
            min_scala = scala

    print(min_scala)

    """
1
20
1 1
2 2
3 3
4 4
5 5
6 6
7 7
8 8
9 9
10 10
11 11 
12 12
13 13 
14 14 
15 15 
16 16 
17 17 
18 18 
19 19 
20 20
    
    """
"""def f(idx, xsum, ysum, S: set):
    global min_scala, visit
    if idx == (1 << n) - 1:
        scala = (xsum ** 2 + ysum ** 2) ** 0.5
        if min_scala > scala:
            min_scala = scala
        return

    for i, p1 in enumerate(ps):
        for j, p2 in enumerate(ps):
            plus = 1 << i | 1 << j
            if i == j or idx & plus > 0:  # or visit[idx|plus]
                continue

            # visit[idx | plus] = 1
            S1 = copy.deepcopy(S)
            S1.add((i, j))
            if S1 in visit:
                continue
            visit.append(S1)
            f(idx | plus, xsum + (p2[0] - p1[0]), ysum + (p2[1] - p1[1]), S1)"""
