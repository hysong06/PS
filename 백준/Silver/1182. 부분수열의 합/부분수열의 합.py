import sys

input = sys.stdin.readline
N, S = map(int, input().split())
nums = list(map(int, input().split()))


def solve(total, i):
    if i == N:
        return 1 if total == S else 0
    return solve(total, i + 1) + solve(total + nums[i], i + 1)


print(solve(0, 0) - (1 if S == 0 else 0))
