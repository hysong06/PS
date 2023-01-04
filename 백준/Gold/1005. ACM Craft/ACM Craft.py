import collections
import sys

input = sys.stdin.readline
for _ in range(int(input())):

    """inits"""
    N, K = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    indegree = [-1] + [0] * N
    cost = [0] + list(map(int, input().split()))

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        indegree[Y] += 1

    W = int(input())

    """ topology sort """
    queue = collections.deque([i for i in range(1, N + 1) if indegree[i] == 0])
    take_time = cost[:]

    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            take_time[nxt] = max(take_time[cur] + cost[nxt], take_time[nxt])
            if indegree[nxt] == 0:
                queue.append(nxt)

    print(take_time[W])
