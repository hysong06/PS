import sys

input = sys.stdin.readline
R, C = map(int, input().split())
graph = [list(map(str, input().rstrip())) for _ in range(R)]
visit = [False] * 26
answer = 1
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def dfs(y: int, x: int, count) -> None:
    global answer
    answer = max(answer, count)

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or ny >= R or nx < 0 or nx >= C or visit[ord(graph[ny][nx]) - 65]:
            continue
        visit[ord(graph[ny][nx]) - 65] = True
        dfs(ny, nx, count + 1)
        visit[ord(graph[ny][nx]) - 65] = False


visit[ord(graph[0][0]) - 65] = True
dfs(0, 0, 1)
print(answer)
