import sys

input = sys.stdin.readline
n = int(input())
levels = [int(input()) for _ in range(n)]


def solution():
    if n == 0:
        return 0

    levels.sort()
    k = int(n * 0.15 + 0.5)
    return int(sum(levels[k : n - k]) / (n - 2 * k) + 0.5)


print(solution())
