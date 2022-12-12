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

visit = [False] * (n + 1)
visit[1] = True

for f in graph[1]:  # friend
    visit[f] = True
    for fof in graph[f]:  # friend of friend
        visit[fof] = True

print(visit.count(True) - 1)  # do not count SangGeun.
