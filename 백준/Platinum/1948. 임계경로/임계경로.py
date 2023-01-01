import collections
import sys

""" inits """
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = collections.defaultdict(dict)
prevs = collections.defaultdict(list)
indegree = [0] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    prevs[b].append(a)
    indegree[b] += 1
start, end = map(int, input().split())
queue = collections.deque()


""" topology sort """
queue.append(start)
start_to = [0] * (n + 1)

while queue:
    cur = queue.popleft()
    for (nxt, cur_to_nxt) in graph[cur].items():
        start_to[nxt] = max(start_to[nxt], start_to[cur] + cur_to_nxt)
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)

max_len = start_to[end]


""" count the edges in the longest path(s). """
queue.append((end, 0))
visit = [False] * (n + 1)
visit[end] = True
counts = 0

while queue:
    cur, cur_to_end = queue.popleft()
    for prev in prevs[cur]:
        prev_to_end = graph[prev][cur] + cur_to_end
        if start_to[prev] + prev_to_end == max_len:
            counts += 1
            if not visit[prev]:
                visit[prev] = True
                queue.append((prev, prev_to_end))


""" answers """
print(max_len)
print(counts)
