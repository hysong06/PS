import heapq
import sys

input = sys.stdin.readline
N = int(input())
cost = [0] * (N + 1)
indegree = [0] * (N + 1)
nexts = [[] for _ in range(N + 1)]

for cur in range(1, N + 1):
    cost[cur], *prevs, _ = map(int, input().split())
    indegree[cur] = len(prevs)
    for prev in prevs:
        nexts[prev].append(cur)


# topological sort
heap = [(cost[i], i) for i in range(1, N + 1) if indegree[i] == 0]
heapq.heapify(heap)
finish = [0] * (N + 1)

while heap:
    times, cur = heapq.heappop(heap)
    finish[cur] = times
    for nxt in nexts[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(heap, (finish[cur] + cost[nxt], nxt))

print(*finish[1:], sep="\n")
