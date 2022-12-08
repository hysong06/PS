import collections
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
check = [list(map(int, input().rstrip())) for _ in range(n)]


def bfs() -> None:
    dr, dc = (1, -1, 0, 0), (0, 0, 1, -1)
    queue = collections.deque()

    # find the start point.
    for i in range(n):
        for j in range(m):
            if check[i][j] == 2:
                queue.append((i, j, 0))
                check[i][j] = 1
                break

    while queue:
        r, c, depth = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= m or check[nr][nc] == 1:
                continue
            if check[nr][nc] > 2:  # if food is found
                print("TAK")
                print(depth + 1)
                return
            queue.append((nr, nc, depth + 1))
            check[nr][nc] = 1

    print("NIE")


bfs()
