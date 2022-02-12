import sys
from itertools import combinations
import queue

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()


def connect(area):
    q = queue.Queue()
    q.put(area[0])
    visit = [area[0]]
    sum = population[area[0] - 1]
    while not q.empty():
        if len(visit) == len(area):
            return (True, sum)
        x = q.get()
        for to in g[x]:
            if to not in visit and to in area:
                visit.append(to)
                q.put(to)
                sum += population[to - 1]
    return (False, 0)


def Input():
    global n, city_list, population, g
    n = int(input())
    city_list = set(range(1, n + 1))
    population = list(map(int, input().split()))
    g = {i + 1: [] for i in range(n)}
    for i in range(n):
        conn = list(map(int, input().split()))
        g[i + 1] += conn[1:]


def Solve():
    diff = 10000000
    for i in range(1, n // 2 + 1):
        nCr = combinations(city_list, i)
        for area in nCr:
            other = city_list - set(area)
            a = connect(list(area))
            b = connect(list(other))
            if a[0] and b[0]:
                diff = min(diff, abs(a[1] - b[1]))
    if diff == 10000000:
        print(-1)
    else:
        print(diff)


if __name__ == "__main__":
    Input()
    Solve()
