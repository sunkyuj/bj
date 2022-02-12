import heapq
from queue import PriorityQueue

mh = []
heapq.heappush(mh, 1)
heapq.heappush(mh, 1)
print(heapq.heappop(mh))
print(heapq.heappop(mh))


pq = PriorityQueue()
pq.put(1)
pq.put(1)
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
