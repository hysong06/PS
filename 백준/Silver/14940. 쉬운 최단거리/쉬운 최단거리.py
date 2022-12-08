import collections
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]

# bfs
queue = collections.deque()
dist = [[-1] * m for _ in range(n)]  # if not visit (i, j), dist[i][j] == -1
dr, dc = (1, -1, 0, 0), (0, 0, 1, -1)

for i in range(n):
    for j in range(m):
        if ground[i][j] == 0:
            dist[i][j] = 0
        elif ground[i][j] == 2:
            queue.append((i, j, 0))

while queue:
    r, c, depth = queue.popleft()
    if dist[r][c] != -1:
        continue
    dist[r][c] = depth

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        queue.append((nr, nc, depth + 1))


for row in dist:
    print(*row)
