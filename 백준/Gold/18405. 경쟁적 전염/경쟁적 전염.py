import collections
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
types = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

dr, dc = (1, -1, 0, 0), (0, 0, 1, -1)
queue = collections.deque(
    sorted(
        (types[i][j], i, j, 0) for i in range(N) for j in range(N) if types[i][j] != 0
    )
)

# bfs
while queue:
    virus, r, c, time = queue.popleft()
    if time == S:
        continue
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N or types[nr][nc] != 0:
            continue
        # virus spreads.
        types[nr][nc] = virus
        queue.append((virus, nr, nc, time + 1))

print(types[X - 1][Y - 1])
