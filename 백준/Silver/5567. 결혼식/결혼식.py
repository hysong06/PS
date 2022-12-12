import collections
import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# bfs
visit = [False] * (n + 1)
visit[1] = True
queue = collections.deque(iterable=[(1, 0)])

while queue:
    student, depth = queue.popleft()
    if depth == 2:
        continue
    for friend in graph[student]:
        if not visit[friend]:
            queue.append((friend, depth + 1))
            visit[friend] = True

print(visit.count(True) - 1)  # do not count SangGeun.
