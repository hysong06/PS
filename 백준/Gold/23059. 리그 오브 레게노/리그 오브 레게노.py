import collections
import sys

input = sys.stdin.readline
graph = collections.defaultdict(list)
indegree = collections.defaultdict(int)
for _ in range(int(input())):
    A, B = input().split()
    graph[A].append(B)
    indegree[B] += 1

waitings = sorted(item for item in graph if indegree[item] == 0)
order = waitings[:]

while waitings:
    temp = []
    for cur in waitings:
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                temp.append(nxt)
    order += (waitings := sorted(temp))

# all items are in graph.keys() now.
print("\n".join(order) if len(order) == len(graph) else -1)
