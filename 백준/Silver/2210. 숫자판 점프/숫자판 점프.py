import sys

input = sys.stdin.readline
board = [input().split() for _ in range(5)]
results = set()
stack = [(i, j, board[i][j]) for i in range(5) for j in range(5)]

# dfs
while stack:
    r, c, path = stack.pop()
    if len(path) == 6:
        results.add(path)
        continue

    for (dr, dc) in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= 5 or nc < 0 or nc >= 5:
            continue
        stack.append((nr, nc, path + board[nr][nc]))

print(len(results))
