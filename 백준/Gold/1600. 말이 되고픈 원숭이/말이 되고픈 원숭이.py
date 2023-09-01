import collections
import sys

input = sys.stdin.readline
K = int(input())
W, H = map(int, input().split())
obstacle = [[*map(lambda x: x == "1", input().split())] for _ in range(H)]
visit = [[[False] * W for _ in range(H)] for _ in range(K + 1)]
queue = collections.deque([(0, 0, 0, 0)])

while queue:
    clop, x, y, level = queue.popleft()
    if x == H - 1 and y == W - 1:
        print(level)
        break

    def monkey_moves(i, j, k):
        if 0 <= j < H and 0 <= k < W and not obstacle[j][k] and not visit[i][j][k]:
            queue.append((i, j, k, level + 1))
            visit[i][j][k] = True

    # 1. move normally
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        monkey_moves(clop, x + dx, y + dy)

    # 2. move like horse
    if clop == K:
        continue
    for dx, dy in ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)):
        monkey_moves(clop + 1, x + dx, y + dy)

else:
    print(-1)
