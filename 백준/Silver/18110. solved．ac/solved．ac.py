import sys

n, *levels = map(int, sys.stdin.read().split())


def solution():
    if n == 0:
        return 0

    k = int(n * 0.15 + 0.5)
    return int(sum(sorted(levels)[k : n - k]) / (n - 2 * k) + 0.5)


print(solution())
