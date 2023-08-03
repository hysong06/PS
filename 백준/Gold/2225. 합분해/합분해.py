import sys

input = sys.stdin.readline
N, K = map(int, input().split())

# the number of cases that sum of i integers is j
memo = [[0] * (N + 1) for _ in range(K + 1)]
for i in range(N + 1):
    memo[1][i] = 1


def solve(k, n):
    if memo[k][n] == 0:
        memo[k][n] = sum(solve(k - 1, n - i) for i in range(n + 1))
    return memo[k][n]


print(solve(K, N) % 1_000_000_000)
