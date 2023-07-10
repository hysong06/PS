import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    dp = [list(map(int, input().split())), list(map(int, input().split()))]

    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    # bottom-up
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    for j in range(2, n):
        dp[0][j] += max(dp[1][j - 2], dp[1][j - 1])
        dp[1][j] += max(dp[0][j - 2], dp[0][j - 1])
    #

    print(max(dp[0][-1], dp[1][-1]))
