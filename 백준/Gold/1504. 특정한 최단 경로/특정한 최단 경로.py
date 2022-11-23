import collections
import heapq
import sys

input = sys.stdin.readline
N, E = map(int, input().split())
graph = collections.defaultdict(list)
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())


def dijkstra(start: int) -> list[int]:
    dist = [float("inf")] * (N + 1)
    heap = [((dist[start] := 0), start)]

    while heap:
        cost_sum, node = heapq.heappop(heap)
        for (link, cost) in graph[node]:
            alt = cost + cost_sum
            if alt <= dist[link]:
                dist[link] = alt
                heapq.heappush(heap, (alt, link))

    return dist


one_to = dijkstra(1)
v1_to = dijkstra(v1)
v2_to = dijkstra(v2)
answer = min(one_to[v1] + v1_to[v2] + v2_to[N], one_to[v2] + v2_to[v1] + v1_to[N])
print(-1 if answer == float("inf") else answer)
