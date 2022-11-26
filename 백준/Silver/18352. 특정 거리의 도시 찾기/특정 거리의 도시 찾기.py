import collections
import sys

input = sys.stdin.readline
N, M, K, X = map(int, input().split())
graph = collections.defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

queue = collections.deque([(X, 0)])
visit = [-1] * (N + 1)  # get the distance from X.

# bfs
while queue:
    node, level = queue.popleft()
    if visit[node] > -1:
        continue
    visit[node] = level

    if level < K:
        for link in graph[node]:
            queue.append((link, level + 1))


answers = [i for i in range(1, N + 1) if visit[i] == K]
if answers:
    print(*answers, sep="\n")
else:
    print(-1)
