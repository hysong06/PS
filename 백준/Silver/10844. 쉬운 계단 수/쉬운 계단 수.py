import sys

N = int(sys.stdin.readline())
dp = [[0] * N for _ in range(10)]

# bottom-up
for r in range(1, 10):
    dp[r][0] = 1

for c in range(1, N):
    dp[0][c] = dp[1][c - 1]
    dp[9][c] = dp[8][c - 1]
    for r in range(1, 9):
        dp[r][c] = dp[r - 1][c - 1] + dp[r + 1][c - 1]

print(sum(dp[r][-1] for r in range(10)) % 1_000_000_000)
