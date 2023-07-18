import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    w, h = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(h)]
    paths = collections.deque()
    fires = collections.deque()
    result = "IMPOSSIBLE"

    for i in range(h):
        for j in range(w):
            if board[i][j] == "*":
                fires.append((i, j))
            elif board[i][j] == "@":
                paths.append((i, j, 0))

    while paths:
        # fires spread first, to save memory
        for _ in range(len(fires)):
            r, c = fires.popleft()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w and board[nr][nc] not in "#*":
                    fires.append((nr, nc))
                    board[nr][nc] = "*"

        # Sang-geun moves
        for _ in range(len(paths)):
            r, c, depth = paths.popleft()

            if r == 0 or r == h - 1 or c == 0 or c == w - 1:
                result = depth + 1
                paths.clear()
                break

            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w and board[nr][nc] == ".":
                    paths.append((nr, nc, depth + 1))
                    board[nr][nc] = "@"  # visit check

    print(result)
