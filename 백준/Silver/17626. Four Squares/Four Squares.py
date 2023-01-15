n = int(input())
dp = [float("inf")] * (n + 1)

dp[0], dp[1] = 0, 1
for target in range(2, n + 1):
    for k in range(1, int(target**0.5) + 1):
        need = target - k**2
        dp[target] = min(dp[need] + 1, dp[target])

print(dp[n])
