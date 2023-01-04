import collections
import heapq
import sys

""" inits """
graph = collections.defaultdict(list)
cost = dict()
indegree = dict()

for line in sys.stdin.readlines():
    data = line.split()
    cur, time, prevs = data[0], int(data[1]), data[-1]

    cost[cur] = time
    if len(data) == 2:  # if there is no prevs
        continue
    indegree[cur] = len(prevs)
    for prev in prevs:
        graph[prev].append(cur)


""" topology sort """
heap = [(cost[k], k) for k in graph if k not in indegree]
heapq.heapify(heap)

while heap:
    path_len, cur = heapq.heappop(heap)
    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            cost[nxt] += path_len
            heapq.heappush(heap, (cost[nxt], nxt))

print(max(cost.values()))
