import collections
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
paper = [input().split() for _ in range(n)]


# bfs
def get_area(queue):
    area = 0

    while queue:
        r, c = queue.popleft()
        area += 1

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= n or nc < 0 or nc >= m or paper[nr][nc] == "0":
                continue
            paper[nr][nc] = "0"
            queue.append((nr, nc))

    return area


# main
count = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if paper[i][j] == "0":
            continue
        paper[i][j] = "0"
        count += 1
        max_area = max(get_area(collections.deque([(i, j)])), max_area)

print(count)
print(max_area)
