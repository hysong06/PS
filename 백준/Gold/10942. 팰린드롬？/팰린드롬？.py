import sys

input = sys.stdin.readline
N = int(input())
nums = ["0", *(input().split())]  # len(nums) == N + 1
memo = [[-1] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    memo[i][i] = 1


def is_palindrome(l, r):
    if memo[l][r] == -1:
        memo[l][r] = int(
            nums[l] == nums[r]
            if r - l == 1
            else nums[l] == nums[r] and is_palindrome(l + 1, r - 1)
        )
    return memo[l][r]


for _ in range(int(input())):
    print(is_palindrome(*map(int, input().split())))
