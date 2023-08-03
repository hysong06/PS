import sys

input = sys.stdin.readline

# len(arr) == len(dp) == N + 1
N = int(input())
arr = ["0", *(input().split())]
dp = [[False] * (N + 1) for _ in range(N + 1)]

# tabulation
dp[N][N] = True
for i in range(1, len(dp) - 1):
    dp[i][i] = True
    dp[i][i + 1] = arr[i] == arr[i + 1]

for j in range(3, len(dp)):
    for i in range(1, j - 1):
        dp[i][j] = arr[i] == arr[j] and dp[i + 1][j - 1]

# result
for _ in range(int(input())):
    S, E = map(int, input().split())
    print(int(dp[S][E]))
