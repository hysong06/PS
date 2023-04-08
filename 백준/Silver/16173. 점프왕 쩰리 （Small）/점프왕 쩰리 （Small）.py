import collections
import sys

input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
queue = collections.deque()
visit = [[False] * N for _ in range(N)]


def queue_push(i, j):
    if i < N and j < N and not visit[i][j]:
        queue.append((i, j))
        visit[i][j] = True


queue_push(0, 0)
while queue:
    i, j = queue.popleft()
    if i == j == N - 1:
        print("HaruHaru")
        break
    queue_push(i + board[i][j], j)
    queue_push(i, j + board[i][j])
else:
    print("Hing")
