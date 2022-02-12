import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()


def find(v):
    if v == root[v]:
        return v
    root[v] = find(root[v])
    return root[v]


def union(v1, v2):  # v1 < v2
    r1 = find(v1)
    r2 = find(v2)
    root[r2] = r1


G = int(input())
P = int(input())

root = [i for i in range(G + 1)]

ans = 0
for i in range(1, P + 1):
    gate_range = int(input())

    docking_loc = find(gate_range)
    if docking_loc == 0:
        break
    ans += 1
    union(docking_loc - 1, docking_loc)
print(ans)

# print(f())
"""
8
8
1
5
3
2
8
4
5
6
"""
