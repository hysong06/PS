import heapq
import sys

input = sys.stdin.readline
N = int(input())
fish = [list(map(int, input().split())) for _ in range(N)]
shark, ate = 2, 0
shark_i, shark_j = None, None

for i in range(N):
    for j in range(N):
        if fish[i][j] == 9:
            shark_i, shark_j = i, j
            fish[shark_i][shark_j] = 0
            break


def eat_fish() -> int:
    global shark, ate, shark_i, shark_j
    heap = [(0, shark_i, shark_j)]
    visit = [[False] * N for _ in range(N)]
    visit[shark_i][shark_j] = True
    delta = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while heap:
        depth, r, c = heapq.heappop(heap)  # heap follows the closest-fish rule
        if shark > fish[r][c] != 0:
            shark_i, shark_j = r, c
            ate, fish[r][c] = ate + 1, 0
            if ate == shark:
                shark, ate = shark + 1, 0
            return depth

        for (dr, dc) in delta:
            nr, nc = r + dr, c + dc
            if (
                not (0 <= nr < N and 0 <= nc < N)
                or fish[nr][nc] > shark
                or visit[nr][nc]
            ):
                continue
            visit[nr][nc] = True
            heapq.heappush(heap, (depth + 1, nr, nc))

    return 0


mealtimes = 0
while (mt := eat_fish()) != 0:
    mealtimes += mt
print(mealtimes)
