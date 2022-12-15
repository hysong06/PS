import sys

sys.setrecursionlimit(10_001)
input = sys.stdin.readline
N, M, K = map(int, input().split())
trash = [[False] * M for _ in range(N)]
for _ in range(K):
    i, j = map(int, input().split())
    trash[i - 1][j - 1] = True


def dfs(r: int, c: int) -> int:  # get the size of trash.
    if r < 0 or r >= N or c < 0 or c >= M or not trash[r][c]:
        return 0
    trash[r][c] = False  # visit check
    return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)


print(max(dfs(i, j) for i in range(N) for j in range(M) if trash[i][j]))
