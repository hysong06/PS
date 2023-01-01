import collections
import sys

""" inits """
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = collections.defaultdict(dict)
indegree = [0] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    indegree[b] += 1
start, end = map(int, input().split())


""" topology sort """
queue = collections.deque()
queue.append(start)
order = []

while queue:
    cur = queue.popleft()
    order.append(cur)
    for (nxt, _) in graph[cur].items():
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

# queue is empty.


""" dp[i] == the longest path from start to i. """
""" can get the longest path from end to start using prevs. """
dp = [0] * (n + 1)
prevs = collections.defaultdict(list)

for cur in order:
    for (nxt, weight) in graph[cur].items():
        path_len = dp[cur] + weight
        if path_len > dp[nxt]:
            dp[nxt] = path_len
            prevs[nxt] = [cur]
        elif path_len == dp[nxt]:
            prevs[nxt].append(cur)


""" count the edges in the longest path(s). """
queue.append(end)
visit = [False] * (n + 1)
visit[end] = True
counts = 0

while queue:
    cur = queue.popleft()
    for prev in prevs[cur]:
        counts += 1
        if not visit[prev]:
            visit[prev] = True
            queue.append(prev)


""" answers """
print(dp[end])
print(counts)
