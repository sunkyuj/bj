import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()


def union(v1, v2):
    r1 = find(v1)
    r2 = find(v2)

    if rank[r1] > rank[r2]:
        root[r2] = r1
    elif rank[r1] < rank[r2]:
        root[r1] = r2
    else:  # rank[r1] == rank[r2]
        root[r2] = r1
        rank[r1] += 1


def find(v):
    if v == root[v]:
        return v
    root[v] = find(root[v])  # 경로 압축
    return root[v]


n, m = map(int, input().split())
roads = []
for _ in range(m):
    a, b, c = map(int, input().split())
    roads.append([a, b, c])
roads.sort(key=lambda x: x[2])

root = [i for i in range(n + 1)]
rank = [0 for _ in range(n + 1)]

c_sum = 0
div = n
for r in roads:
    if div == 2:
        break

    a, b, c = r[0], r[1], r[2]
    if find(a) == find(b):
        continue

    union(a, b)
    div -= 1
    c_sum += c

print(c_sum)
# print(root)
