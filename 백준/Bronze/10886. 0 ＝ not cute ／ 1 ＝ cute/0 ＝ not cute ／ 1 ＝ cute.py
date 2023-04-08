import sys

N = int(sys.stdin.readline())
print(
    "Junhee is "
    + ("" if round(sum(int(input()) for _ in range(N)) / N) == 1 else "not ")
    + "cute!"
)