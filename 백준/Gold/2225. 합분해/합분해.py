import sys

input = sys.stdin.readline
N, K = map(int, input().split())
memo = [[0] * (N + 1) for _ in range(K + 1)]

for n in range(N + 1):
    memo[1][n] = 1

for k in range(2, K + 1):
    for n in range(0, N + 1):
        for m in range(0, n + 1):
            memo[k][n] += memo[k - 1][n - m]
            memo[k][n] %= 1_000_000_000

print(memo[K][N])
