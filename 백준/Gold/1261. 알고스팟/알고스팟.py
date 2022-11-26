import heapq
import sys

input = sys.stdin.readline
M, N = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]


def solution() -> int:
    heap = [(0, 0, 0)]
    visit = [[False] * M for _ in range(N)]
    visit[0][0] = True

    while heap:
        broken_walls, i, j = heapq.heappop(heap)
        if i == N - 1 and j == M - 1:
            return broken_walls

        for (di, dj) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M or visit[ni][nj]:
                continue
            visit[ni][nj] = True
            heapq.heappush(heap, (broken_walls + maze[ni][nj], ni, nj))


print(solution())
