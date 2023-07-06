import collections
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
campus = [list(input().rstrip("\n")) for _ in range(N)]
queue = collections.deque(
    [(i, j) for i in range(N) for j in range(M) if campus[i][j] == "I"]
)
encounter = 0

# bfs
while queue:
    r, c = queue.popleft()

    for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= M or campus[nr][nc] == "X":
            continue

        if campus[nr][nc] == "P":
            encounter += 1

        queue.append((nr, nc))
        campus[nr][nc] = "X"  # visit check

print(encounter if encounter > 0 else "TT")
