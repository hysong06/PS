import collections
import sys

input = sys.stdin.readline

# if wall is on (i, j), wall[i][j] == True.
N, M = map(int, input().split())
wall = [list(map(lambda x: bool(int(x)), input().rstrip())) for _ in range(N)]


def bfs() -> int:
    """
    dist[0][i][j] == the shortest path to (i, j) 'without a crushed wall'.
    dist[1][i][j] == the shortest path to (i, j) 'with a crushed wall'.
    cf. if dist[crushed][i][j] == 0, (crushed, i, j) is not visited.
    """
    dist = [[[0] * M for _ in range(N)] for _ in range(2)]
    dist[0][0][0] = dist[1][0][0] = 1
    queue = collections.deque(iterable=[(0, 0, 0)])
    dr, dc = (1, -1, 0, 0), (0, 0, 1, -1)

    while queue:
        crushed, r, c = queue.popleft()
        if r == N - 1 and c == M - 1:
            return dist[crushed][r][c]

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if not wall[nr][nc]:
                if dist[crushed][nr][nc] == 0:
                    queue.append((crushed, nr, nc))
                    dist[crushed][nr][nc] = dist[crushed][r][c] + 1
            elif crushed == 0:
                queue.append((1, nr, nc))
                dist[1][nr][nc] = dist[crushed][r][c] + 1

    return -1


print(bfs())
