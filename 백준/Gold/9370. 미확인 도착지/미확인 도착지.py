import collections
import heapq
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    # initializations
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = collections.defaultdict(list)
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    candidates = (int(input()) for _ in range(t))

    # solution
    def dijkstra(start: int) -> list[int]:
        heap = [(0, start)]
        dist = [50_000_001] * (n + 1)  # max(m) * max(d) == 50_000_000
        dist[start] = 0

        while heap:
            path_len, node = heapq.heappop(heap)
            if dist[node] < path_len:
                continue
            for (link, length) in graph[node]:
                alt = path_len + length
                if alt < dist[link]:
                    dist[link] = alt
                    heapq.heappush(heap, (alt, link))

        return dist

    s_to = dijkstra(s)
    g_to = dijkstra(g)
    h_to = dijkstra(h)

    print(
        *sorted(
            c
            for c in candidates
            if (s_to[c] == s_to[h] + h_to[g] + g_to[c])
            or (s_to[c] == s_to[g] + g_to[h] + h_to[c])
        ),
        sep="\n",
    )
