import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    prevs = [[] for _ in range(N + 1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        prevs[Y].append(X)
    W = int(input())
    take_time = [-1] * (N + 1)

    def dfs(cur: int) -> int:
        if take_time[cur] == -1:
            take_time[cur] = cost[cur] + (
                max(dfs(prev) for prev in prevs[cur]) if prevs[cur] else 0
            )
        return take_time[cur]

    print(dfs(W))
