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


def dijkstra(start: int, end: int) -> int:
    visit = set()
    heap = [(0, start)]

    while heap:
        cost_sum, node = heapq.heappop(heap)
        if node == end:
            return cost_sum
        if node in visit:
            continue

        visit.add(node)
        for (link, cost) in graph[node]:
            heapq.heappush(heap, (cost + cost_sum, link))

    return -1


path1 = [dijkstra(1, v1), dijkstra(v1, v2), dijkstra(v2, N)]
path2 = [dijkstra(1, v2), dijkstra(v2, v1), dijkstra(v1, N)]

if -1 in path1 and -1 in path2:
    print(-1)
elif -1 in path1:
    print(sum(path2))
elif -1 in path2:
    print(sum(path1))
else:
    print(min(sum(path1), sum(path2)))
