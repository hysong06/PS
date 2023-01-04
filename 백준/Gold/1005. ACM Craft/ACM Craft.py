import sys

sys.setrecursionlimit(10_000)
input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    prevs = [[] for _ in range(N + 1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        prevs[Y].append(X)
    W = int(input())
    visit = [False] * (N + 1)

    def dfs(cur: int) -> int:
        if not visit[cur]:
            visit[cur] = True
            cost[cur] += max(dfs(prev) for prev in prevs[cur]) if prevs[cur] else 0
        return cost[cur]

    print(dfs(W))
