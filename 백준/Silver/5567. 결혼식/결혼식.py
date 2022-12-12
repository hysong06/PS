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

visit = {1}
for f in graph[1]:  # friend
    visit.add(f)
    for fof in graph[f]:  # friend of friend
        visit.add(fof)

print(len(visit) - 1)  # do not count SangGeun.
