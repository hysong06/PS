import collections
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = collections.defaultdict(list)
indegree = collections.defaultdict(int)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

order = []
queue = collections.deque([i for i in range(1, N + 1) if indegree[i] == 0])

while queue:
    cur = queue.popleft()
    order.append(cur)
    for nxt in graph[cur]:
        indegree[nxt] -= 1  # remove the edge (cur, link)
        if indegree[nxt] == 0:
            queue.append(nxt)

print(*order)
