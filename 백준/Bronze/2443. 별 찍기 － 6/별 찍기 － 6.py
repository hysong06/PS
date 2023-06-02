import sys

input = sys.stdin.readline
N = int(input())

for i in range(N):
    print(("*" * (2 * (N - i) - 1)).rjust(2 * N - 1 - i, " "))
