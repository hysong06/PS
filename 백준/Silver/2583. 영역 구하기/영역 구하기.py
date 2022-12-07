import sys

sys.setrecursionlimit(10_001)
input = sys.stdin.readline
M, N, K = map(int, input().split())
visit = [[False] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    y1, y2 = M - y1, M - y2
    for i in range(y2, y1):
        for j in range(x1, x2):
            visit[i][j] = True


def dfs(r: int, c: int) -> int:
    if r < 0 or r >= M or c < 0 or c >= N or visit[r][c]:
        return 0
    visit[r][c] = True
    return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)


widths = [dfs(i, j) for i in range(M) for j in range(N) if not visit[i][j]]
print(len(widths))
print(*sorted(widths))
