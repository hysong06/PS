import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))


def dfs(start, end):
    stack = [(start, 0)]
    visit = [False] * (N + 1)

    while True:
        cur, path_len = stack.pop()
        if cur == end:
            return path_len

        if visit[cur]:
            continue
        visit[cur] = True

        for nxt, weight in graph[cur]:
            if visit[nxt]:
                continue
            stack.append((nxt, path_len + weight))


for _ in range(M):
    print(dfs(*map(int, input().split())))
