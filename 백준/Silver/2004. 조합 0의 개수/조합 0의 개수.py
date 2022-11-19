import sys

input = sys.stdin.readline
n, m = map(int, input().split())


# return the number of factor in factorial(src).
def count_factor(src: int, factor: int) -> int:
    count = 0
    while src != 0:
        src //= factor
        count += src
    return count


print(
    min(
        count_factor(n, 2) - count_factor(m, 2) - count_factor(n - m, 2),
        count_factor(n, 5) - count_factor(m, 5) - count_factor(n - m, 5),
    )
)
