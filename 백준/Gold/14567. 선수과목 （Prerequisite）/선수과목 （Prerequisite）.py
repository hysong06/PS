import collections
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

depths = [1] * (N + 1)
queue = collections.deque([i for i in range(1, N + 1) if indegree[i] == 0])

while queue:
    cur = queue.popleft()
    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)
            depths[nxt] = depths[cur] + 1

print(*depths[1:])
