import sys

input = sys.stdin.readline
N, M = map(int, input().split())

"""
make a 2D prefix-sum table:
    psum[r][c] ==
        sum(psum[i][j] for i in range(1, r + 1) for j in range(1, c + 1))
"""
psum = [[0] * (N + 1)]
for _ in range(N):
    psum.append([0] + list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        psum[i][j] += psum[i][j - 1] + psum[i - 1][j] - psum[i - 1][j - 1]

# main
for _ in range(M):
    x1, y1, x2, y2 = map(int, map(int, input().split()))
    print(psum[x2][y2] - psum[x2][y1 - 1] - psum[x1 - 1][y2] + psum[x1 - 1][y1 - 1])
