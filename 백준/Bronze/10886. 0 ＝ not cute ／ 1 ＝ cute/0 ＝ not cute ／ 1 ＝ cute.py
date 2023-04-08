import sys

input = sys.stdin.readline
N = int(input())

print(
    "Junhee is "
    + ("" if round(sum(int(input()) for _ in range(N)) / N) == 1 else "not ")
    + "cute!"
)
