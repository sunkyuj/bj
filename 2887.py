import sys
import heapq

# sys.setrecursionlimit(10 ** 8)  # pypy 제출시 삭제!
input = lambda: sys.stdin.readline().rstrip()
# in_range = lambda y,x: 0<=y<n and 0<=x<m


def find(v):
    if v == root[v]:
        return v
    root[v] = find(root[v])
    return root[v]


def union(v1, v2):
    r1 = find(v1)
    r2 = find(v2)
    if r1 > r2:
        r1, r2 = r2, r1  # r1 <= r2
    root[r2] = r1  # 더 작은 인덱스가 root가 됨


n = int(input())
planets = [0 for _ in range(n)]
root = [i for i in range(n)]

for i in range(n):
    x, y, z = map(int, input().split())
    planets[i] = (x, y, z, i)

xsort = sorted(planets, key=lambda x: x[0])  # x에 대하여 정렬
ysort = sorted(planets, key=lambda x: x[1])  # y에 대하여 정렬
zsort = sorted(planets, key=lambda x: x[2])  # z에 대하여 정렬

mh = []  # (len,a,b)
for i in range(n - 1):
    heapq.heappush(
        mh, (abs(xsort[i][0] - xsort[i + 1][0]), xsort[i][3], xsort[i + 1][3])
    )  # x
    heapq.heappush(
        mh, (abs(ysort[i][1] - ysort[i + 1][1]), ysort[i][3], ysort[i + 1][3])
    )  # y
    heapq.heappush(
        mh, (abs(zsort[i][2] - zsort[i + 1][2]), zsort[i][3], zsort[i + 1][3])
    )  # z

cnt = 0
ans = 0
while cnt < n - 1:  # 크루스칼 알고리즘
    l, a, b = heapq.heappop(mh)
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        ans += l
print(ans)
