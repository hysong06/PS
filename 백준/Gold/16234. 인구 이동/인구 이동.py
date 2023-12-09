import sys

sys.setrecursionlimit(2500)
input = sys.stdin.readline
N, L, R = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]

days = 0

while True:
    visit = [[False] * N for _ in range(N)]
    tree = []

    def dfs(r, c):
        if visit[r][c]:
            return
        visit[r][c] = True
        tree.append((r, c))

        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = r + dr, c + dc
            if (0 <= nr < N) and (0 <= nc < N) and (L <= abs(A[r][c] - A[nr][nc]) <= R):
                dfs(nr, nc)

    # an union is a chunk where the all nations open the borders to each other
    unions = []

    for i, j in ((i, j) for i in range(N) for j in range(N)):
        dfs(i, j)
        if len(tree) > 1:
            unions.append(tree[:])
        tree.clear()

    if not unions:
        break

    for union in unions:
        result = sum(A[i][j] for i, j in union) // len(union)
        for i, j in union:
            A[i][j] = result

    days += 1

print(days)
