import sys

input = sys.stdin.readline
N = int(input())
heights = [list(map(int, input().split())) for _ in range(N)]


def calc_safe_area(rains: int) -> int:
    h = [heights[i][:] for i in range(N)]
    visit = [[False] * N for _ in range(N)]

    # if h[i][j] is flooded, h[i][j] is unvisitable,
    # and regard it as already visited.
    for i in range(N):
        for j in range(N):
            if h[i][j] <= rains:
                visit[i][j] = True

    # dfs
    stack = [(i, j, True) for i in range(N) for j in range(N) if not visit[i][j]]
    dr, dc = (1, -1, 0, 0), (0, 0, 1, -1)
    safe_area = 0

    while stack:
        r, c, start = stack.pop()
        if visit[r][c]:
            continue
        visit[r][c] = True
        if start:
            safe_area += 1

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N or visit[nr][nc]:
                continue
            stack.append((nr, nc, False))

    return safe_area


min_h, max_h = min(map(min, heights)), max(map(max, heights))
print(max(calc_safe_area(i) for i in range(min_h, max_h + 1)) or 1)
