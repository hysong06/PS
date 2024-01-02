import sys
import heapq

input = sys.stdin.readline

for _ in range(int(input())):
    # init
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    # Dijkstra's algorithm
    heap = [(0, c)]
    dist = [float("inf")] * (n + 1)
    dist[c] = 0

    while heap:
        time, a = heapq.heappop(heap)
        if dist[a] < time:
            continue
        for b, s in graph[a]:
            alt = time + s
            if alt < dist[b]:
                dist[b] = alt
                heapq.heappush(heap, (alt, b))

    result = [v for v in dist if v != float("inf")]
    print(len(result), max(result))
