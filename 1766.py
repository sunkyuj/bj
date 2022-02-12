import sys
import heapq

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
in_degree = [0 for _ in range(n + 1)]  # in_degree[x]  <-- x번 문제의 들어오는 차수
outs = {}  # outs[a] = {b,c,d,...}  <-- 문제 a 는 b,c,d,... 보다 먼저 풀어야한다.

for i in range(m):
    a, b = map(int, input().split())
    in_degree[b] += 1  # a->b 이므로 b의 in_degree를 하나 늘림
    outs.setdefault(a, set())  # outs는 set을 value로 갖는 딕셔너리
    outs[a].add(b)  # a->b

minh = []  # 최소힙
for i in range(1, n + 1):
    if in_degree[i] == 0:
        heapq.heappush(minh, i)  # 최소힙에  차수가 0인 문제들를 넣어줌

for i in range(n):
    x = heapq.heappop(minh)  # 차수가 가장 낮고 문제 번호도 가장 낮은 문제를 pop
    print(x, end=" ")
    while x in outs and outs[x]:  # 문제 x가 가리키고 있는 문제들만큼 반복
        out = outs[x].pop()  # 문제 x가 가리키고 있는 문제 하나 pop
        in_degree[out] -= 1  # 해당 문제의 차수 하나 줄임
        if in_degree[out] == 0:  # 만약 그 문제의 차수가 0이 되면, 이제 풀 수 있게 되므로 최소힙에 집어넣음
            heapq.heappush(minh, out)
