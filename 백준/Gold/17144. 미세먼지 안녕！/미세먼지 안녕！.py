from collections import deque
import sys

input = sys.stdin.readline
R, C, T = map(int, input().split())
A = [deque(map(int, input().split())) for _ in range(R)]
x, y = 0, 0  # the position of the air cleaner

for i in range(R):
    if A[i][0] == -1:
        x = i
        y = x + 1
        A[x][0] = A[y][0] = 0
        break


def dust_spread():
    result = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if A[r][c] == 0:
                continue

            amount = A[r][c] // 5
            spread = 0

            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= R or nc < 0 or nc >= C or (nc == 0 and (nr == x or nr == y)):
                    continue
                result[nr][nc] += amount
                spread += 1

            result[r][c] += A[r][c] - amount * spread

    for i in range(R):
        for j in range(C):
            A[i][j] = result[i][j]


def upper_circulation():
    top_left = A[0][0]

    A[x].rotate()
    A[0].rotate(-1)

    for i in range(x - 1):
        A[i][-1] = A[i + 1][-1]
    A[x - 1][-1] = A[x][0]

    A[x][0] = 0
    for i in range(x - 1, 1, -1):
        A[i][0] = A[i - 1][0]
    A[1][0] = top_left


def lower_circulation():
    bottom_left = A[-1][0]

    A[y].rotate()
    A[-1].rotate(-1)

    for i in range(R - 1, y + 1, -1):
        A[i][-1] = A[i - 1][-1]
    A[y + 1][-1] = A[y][0]

    A[y][0] = 0
    for i in range(y + 1, R - 2):
        A[i][0] = A[i + 1][0]
    A[R - 2][0] = bottom_left


# main
for _ in range(T):
    dust_spread()
    upper_circulation()
    lower_circulation()

print(sum(map(sum, A)))
