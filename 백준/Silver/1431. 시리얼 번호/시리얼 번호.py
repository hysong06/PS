import functools
import sys


def compare(a: str, b: str):
    if a == b:
        return 0

    """ condition 1 """
    if len(a) < len(b):
        return -1
    if len(a) > len(b):
        return 1

    """ condition 2 """
    x = sum(int(ch) for ch in a if ch.isdigit())
    y = sum(int(ch) for ch in b if ch.isdigit())

    if x < y:
        return -1
    if x > y:
        return 1

    """ condition 3 """
    if a < b:
        return -1
    return 1  # if a > b


input = sys.stdin.readline
N = int(input())
print(
    "\n".join(
        sorted([input().rstrip() for _ in range(N)], key=functools.cmp_to_key(compare))
    )
)
