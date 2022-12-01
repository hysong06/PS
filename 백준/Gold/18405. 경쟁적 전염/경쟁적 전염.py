import collections
import heapq
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
types = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

dr, dc = (1, -1, 0, 0), (0, 0, 1, -1)
queue = collections.deque()
heap = [(types[i][j], i, j) for i in range(N) for j in range(N) if types[i][j] != 0]
heapq.heapify(heap)
while heap:
    _, i, j = heapq.heappop(heap)
    queue.append((i, j, 0))

# bfs
while queue:
    r, c, time = queue.popleft()
    if time == S:
        continue
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N or types[nr][nc] > 0:
            continue
        # virus spreads.
        types[nr][nc] = types[r][c]
        queue.append((nr, nc, time + 1))

print(types[X - 1][Y - 1])
