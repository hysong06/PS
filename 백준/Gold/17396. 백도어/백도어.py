import collections
import heapq
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
exposed = list(map(int, input().split()))
exposed[-1] = 0
graph = collections.defaultdict(list)
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))


def dijkstra() -> int:
    heap = [(0, 0)]
    dist = [float("inf")] * N
    dist[0] = 0

    while heap:
        time_sum, node = heapq.heappop(heap)
        if time_sum > dist[node]:
            continue
        for (link, time) in graph[node]:
            alt = time_sum + time
            if alt < dist[link] and not exposed[link]:
                dist[link] = alt
                heapq.heappush(heap, (alt, link))

    return -1 if dist[-1] == float("inf") else dist[-1]


print(dijkstra())
