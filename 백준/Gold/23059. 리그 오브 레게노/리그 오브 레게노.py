import collections
import sys

input = sys.stdin.readline
graph = collections.defaultdict(list)
indegree = collections.defaultdict(int)
for _ in range(int(input())):
    A, B = input().split()
    graph[A].append(B)
    indegree[B] += 1

order = []
waitings = sorted(item for item in graph if indegree[item] == 0)

while waitings:
    order.extend(waitings)

    temp = []
    for cur in waitings:
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                temp.append(nxt)
    waitings = sorted(temp)

print("\n".join(order) if len(order) == len(set(graph) | set(indegree)) else -1)
