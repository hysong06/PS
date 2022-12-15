import collections
import sys

input = sys.stdin.readline

while True:
    # inits
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        break

    cube = []
    for _ in range(L):
        cube.append([list(map(str, input().rstrip())) for _ in range(R)])
        input()
    delta = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    queue = collections.deque()

    # find the start point.
    for k in range(L):
        for i in range(R):
            for j in range(C):
                if cube[k][i][j] == "S":
                    queue.append((k, i, j, 0))
                    break

    def bfs() -> str:
        while queue:
            l, r, c, depth = queue.popleft()
            depth += 1  # next depth, not current depth.

            for (dl, dr, dc) in delta:
                nl, nr, nc = l + dl, r + dr, c + dc
                if nl < 0 or nl >= L or nr < 0 or nr >= R or nc < 0 or nc >= C:
                    continue
                if cube[nl][nr][nc] == "E":
                    return f"Escaped in {depth} minute(s)."
                if cube[nl][nr][nc] == ".":
                    queue.append((nl, nr, nc, depth))
                    cube[nl][nr][nc] = "#"  # visit check

        return "Trapped!"

    print(bfs())
