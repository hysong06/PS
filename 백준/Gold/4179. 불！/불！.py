import collections
import sys

input = sys.stdin.readline
R, C = map(int, input().split())
maze = [list(input().rstrip("\n")) for _ in range(R)]
jihun = collections.deque()
fires = collections.deque()
result = "IMPOSSIBLE"

for i in range(R):
    for j in range(C):
        if maze[i][j] == "F":
            fires.append((i, j))
        elif maze[i][j] == "J":
            jihun.append((i, j, 0))
            maze[i][j] = "V"  # visit


while jihun:
    # fires spread first, to save memory
    for _ in range(len(fires)):
        r, c = fires.popleft()
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] not in "#F":
                maze[nr][nc] = "F"
                fires.append((nr, nc))

    # jihun moves
    for _ in range(len(jihun)):
        r, c, depth = jihun.popleft()

        if r == 0 or r == R - 1 or c == 0 or c == C - 1:
            result = depth + 1
            jihun.clear()
            break

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] == ".":
                jihun.append((nr, nc, depth + 1))
                maze[nr][nc] = "V"

print(result)
