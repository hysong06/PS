import sys


def digit_of(x: str) -> int:
    if len(x) == 1:
        return 10
    if x[0] == "0":
        if x[1] == "x":
            return 16
        else:
            return 8
    return 10


X = sys.stdin.readline().rstrip("\n")
print(int(X, digit_of(X)))
