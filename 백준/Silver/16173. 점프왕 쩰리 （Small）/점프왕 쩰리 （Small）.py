import collections
import sys

input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
queue = collections.deque()
visit = [[False] * N for _ in range(N)]

queue.append((0, 0))
visit[0][0] = True

while queue:
    i, j = queue.popleft()
    if i == j == N - 1:
        print("HaruHaru")
        break

    step = board[i][j]
    if i + step < N and not visit[i + step][j]:  # move down
        visit[i + step][j] = True
        queue.append((i + step, j))
    if j + step < N and not visit[i][j + step]:  # move right
        visit[i][j + step] = True
        queue.append((i, j + step))
else:
    print("Hing")
