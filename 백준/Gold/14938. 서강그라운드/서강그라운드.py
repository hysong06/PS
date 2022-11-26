import collections
import heapq
import sys

input = sys.stdin.readline
n, m, r = map(int, input().split())
drops = [0] + list(map(int, input().split()))
graph = collections.defaultdict(list)
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))


def dijkstra(start: int) -> int:
    heap = [(0, start)]
    dist = [float("inf")] * (n + 1)
    dist[start] = 0

    while heap:
        path_len, node = heapq.heappop(heap)
        if dist[node] < path_len:
            continue
        for (nxt, length) in graph[node]:
            alt = path_len + length
            if alt < dist[nxt] and alt <= m:
                dist[nxt] = alt
                heapq.heappush(heap, (alt, nxt))

    return sum(drops[i] for i in range(1, n + 1) if dist[i] != float("inf"))


print(max(dijkstra(i) for i in range(1, n + 1)))
