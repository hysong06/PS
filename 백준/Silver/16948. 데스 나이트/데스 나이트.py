import collections
import sys

input = sys.stdin.readline
N = int(input())
r1, c1, r2, c2 = map(int, input().split())

queue = collections.deque([(r1, c1)])
dist = [[-1] * N for _ in range(N)]
dist[r1][c1] = 0
delta = ((-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1))

# bfs
while queue:
    r, c = queue.popleft()
    if r == r2 and c == c2:
        print(dist[r][c])
        break

    for (dr, dc) in delta:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= N or dist[nr][nc] != -1:
            continue
        queue.append((nr, nc))
        dist[nr][nc] = dist[r][c] + 1
else:
    print(-1)
