import heapq
import sys

input = sys.stdin.readline
n = int(input())
rooms = [list(map(int, input().rstrip())) for _ in range(n)]


def solution() -> int:
    heap = [(0, 0, 0)]
    visit = [[False] * n for _ in range(n)]
    visit[0][0] = True

    while heap:
        changes, i, j = heapq.heappop(heap)
        if i == j == n - 1:
            return changes

        for (di, dj) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= n or visit[ni][nj]:
                continue
            visit[ni][nj] = True
            heapq.heappush(heap, (changes + int(rooms[ni][nj] == 0), ni, nj))


print(solution())
