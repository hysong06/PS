import collections
import heapq
import sys

input = sys.stdin.readline
n, m, r = map(int, input().split())
drops = [0] + list(map(int, input().split()))  # len(drops) == n
graph = collections.defaultdict(list)
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))


def dijkstra(start: int) -> int:
    heap = [(0, start)]
    reachable = set()

    while heap:
        cur_len, node = heapq.heappop(heap)
        if node in reachable:
            continue
        reachable.add(node)

        for (nxt, length) in graph[node]:
            if nxt in reachable or (next_len := cur_len + length) > m:
                continue
            heapq.heappush(heap, (next_len, nxt))

    return sum(drops[i] for i in range(1, n + 1) if i in reachable)


print(max(dijkstra(i) for i in range(1, n + 1)))
