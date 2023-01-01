import heapq
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

heap = [i for i in range(1, N + 1) if indegree[i] == 0]
heapq.heapify(heap)
order = []

while heap:
    cur = heapq.heappop(heap)
    order.append(cur)
    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(heap, nxt)

print(*order)
