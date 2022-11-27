import sys

input = sys.stdin.readline
R, C = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(R)]

answer = 1
dr, dc = (1, -1, 0, 0), (0, 0, 1, -1)
visit = [False] * 26


def dfs(r: int, c: int, depth: int) -> None:
    global answer
    answer = max(depth, answer)

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            continue

        idx = ord(board[nr][nc]) - 65  # if board[nr][nc] == "A", idx == 0
        if not visit[idx]:
            visit[idx] = True
            dfs(nr, nc, depth + 1)
            visit[idx] = False


visit[ord(board[0][0]) - 65] = True
dfs(0, 0, 1)
print(answer)
