import collections
import heapq
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
exposed = input().split()
graph = collections.defaultdict(list)
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))


def dijkstra() -> int:
    heap = [(0, 0)]
    dist = [float("-inf") if exposed[i] == "1" else float("inf") for i in range(N)]
    dist[0], dist[-1] = 0, float("inf")

    while heap:
        time_sum, node = heapq.heappop(heap)
        if time_sum > dist[node]:
            continue
        if node == N - 1:
            return time_sum

        for (link, time) in graph[node]:
            alt = time_sum + time
            if alt < dist[link]:
                dist[link] = alt
                heapq.heappush(heap, (alt, link))

    return -1


print(dijkstra())
