import sys

N = int(sys.stdin.readline())

# bottom-up
dp = [0, *([1] * 9)]
for _ in range(N - 1):
    dp = [dp[1], *(dp[i - 1] + dp[i + 1] for i in range(1, 9)), dp[8]]

print(sum(dp) % 1_000_000_000)
