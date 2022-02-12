import sys
from queue import PriorityQueue

sys.setrecursionlimit(10 ** 8)  # pypy 제출시 삭제!
input = lambda: sys.stdin.readline().rstrip()
# in_range = lambda y,x: 0<=y<n and 0<=x<m

n = int(input())
degree = [0 for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    degree[a] += 1
    degree[b] += 1

pq = PriorityQueue()
for i in range(1, n + 1):
    pq.put((-degree[i], i))

cnt = 0
ans = 0
while not pq.empty() and cnt < n:
    d = -pq.get()[0]
    cnt += d
    ans += 1
print(ans)
