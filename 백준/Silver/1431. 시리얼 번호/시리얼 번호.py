import functools
import sys


def compare(a: str, b: str) -> int:
    if a == b:
        return 0

    """ condition 1 """
    if len(a) != len(b):
        return len(a) - len(b)

    """ condition 2 """
    x = sum(int(ch) for ch in a if ch.isdigit())
    y = sum(int(ch) for ch in b if ch.isdigit())
    if x != y:
        return x - y

    """ condition 3 """
    return -1 if a < b else 1


# main
input = sys.stdin.readline
N = int(input())
serials = [input().rstrip("\n") for _ in range(N)]
print("\n".join(sorted(serials, key=functools.cmp_to_key(compare))))
