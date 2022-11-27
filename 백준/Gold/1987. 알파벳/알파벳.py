import sys

input = sys.stdin.readline
R, C = map(int, input().split())
board = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(R)]
# each alphabet is replaced with its order. (A-Z == 0-25)

answer = 1
dr, dc = (1, -1, 0, 0), (0, 0, 1, -1)
visit = [False] * 26


def dfs(r: int, c: int, depth: int) -> None:
    global answer
    answer = max(depth, answer)

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nr >= R or nc < 0 or nc >= C or visit[board[nr][nc]]:
            continue
        visit[board[nr][nc]] = True
        dfs(nr, nc, depth + 1)
        visit[board[nr][nc]] = False


visit[board[0][0]] = True
dfs(0, 0, 1)
print(answer)
