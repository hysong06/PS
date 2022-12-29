import collections
import heapq
import sys

input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    S, D = map(int, input().split())
    prevs = collections.defaultdict(list)
    graph = collections.defaultdict(dict)
    for _ in range(M):
        U, V, P = map(int, input().split())
        graph[U][V] = P
        prevs[V].append(U)

    def dijkstra(start: int) -> list[int]:
        dist = [float("inf")] * N
        dist[start] = 0
        heap = [(0, start)]

        while heap:
            path_len, cur = heapq.heappop(heap)
            if path_len > dist[cur]:
                continue
            for (nxt, weight) in graph[cur].items():
                alt = path_len + weight
                if alt < dist[nxt]:
                    dist[nxt] = alt
                    heapq.heappush(heap, (alt, nxt))

        return dist

    # remove the routes in the shortest path using reversed-bfs.
    shortest = dijkstra(S)
    queue = collections.deque()
    queue.append((D, 0))

    while queue:
        cur, cur_to_D = queue.popleft()
        for prev in prevs[cur]:
            if cur not in graph[prev]:  # if (prev, cur) is already removed
                continue
            path_len = shortest[prev] + graph[prev][cur] + cur_to_D
            if path_len == shortest[D]:
                queue.append((prev, graph[prev][cur] + cur_to_D))
                del graph[prev][cur]

    answer = dijkstra(S)[D]
    print(-1 if answer == float("inf") else answer)
