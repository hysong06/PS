import sys

"""inits"""
input = sys.stdin.readline
N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]


"""convex figures"""
answer = max(
    mat[i][j]
    + mat[i][j - 1]
    + mat[i][j + 1]
    + mat[i - 1][j]
    + mat[i + 1][j]
    - min(mat[i][j - 1], mat[i][j + 1], mat[i - 1][j], mat[i + 1][j])
    for i in range(1, N - 1)
    for j in range(1, M - 1)
)
for i in range(1, N - 1):
    answer = max(
        answer,
        mat[i - 1][0] + mat[i][0] + mat[i + 1][0] + mat[i][1],
        mat[i - 1][-1] + mat[i][-1] + mat[i + 1][-1] + mat[i][-2],
    )
for j in range(1, M - 1):
    answer = max(
        answer,
        mat[0][j - 1] + mat[0][j] + mat[0][j + 1] + mat[1][j],
        mat[-1][j - 1] + mat[-1][j] + mat[-1][j + 1] + mat[-2][j],
    )


"""the others"""
visit = [[False] * M for _ in range(N)]
delta = ((1, 0), (-1, 0), (0, 1), (0, -1))


def dfs(r: int, c: int, value: int, depth: int) -> None:
    global answer
    if depth == 4:
        answer = max(value, answer)
        return

    visit[r][c] = True
    for (dr, dc) in delta:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= M or visit[nr][nc]:
            continue
        dfs(nr, nc, value + mat[nr][nc], depth + 1)
    visit[r][c] = False


for i in range(N):
    for j in range(M):
        dfs(i, j, mat[i][j], 1)


"""result"""
print(answer)
