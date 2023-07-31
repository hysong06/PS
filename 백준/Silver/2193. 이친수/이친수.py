import sys

N = int(sys.stdin.readline())
dp = [[0] * N for _ in range(2)]

dp[1][0] = 1
for j in range(N - 1):
    dp[0][j + 1] += dp[0][j] + dp[1][j]
    dp[1][j + 1] += dp[0][j]

print(dp[0][-1] + dp[1][-1])
