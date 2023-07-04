import sys


def power(a, b, c):
    if b == 1:
        return a % c

    temp = power(a, b // 2, c)
    return (temp * temp * (a if b & 1 else 1)) % c


A, B, C = map(int, sys.stdin.readline().split())
print(power(A, B, C))
