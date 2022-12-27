import re
import sys

input = sys.stdin.readline
N = int(input())
print(
    *sorted(num for _ in range(N) for num in map(int, re.findall("\d+", input()))),
    sep="\n"
)
