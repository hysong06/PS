import heapq
import sys

take_time = [0] * 26  # can exist-check.
indegree = [0] * 26
graph = [[] for _ in range(26)]

for line in sys.stdin.readlines():
    data = line.split()
    cur, cost, prevs = (
        ord(data[0]) - 65,
        int(data[1]),
        tuple(map(lambda e: ord(e) - 65, data[-1])),
    )

    take_time[cur] = cost
    if len(data) == 3:
        indegree[cur] = len(prevs)
        for prev in prevs:
            graph[prev].append(cur)


""" topology sort """
heap = [(take_time[k], k) for k in range(26) if take_time[k] != 0 and indegree[k] == 0]
heapq.heapify(heap)

while heap:
    path_len, cur = heapq.heappop(heap)
    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            take_time[nxt] += path_len
            heapq.heappush(heap, (take_time[nxt], nxt))

print(max(take_time))
