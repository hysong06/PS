import re
import sys

input = sys.stdin.readline
print(
    *sorted(
        int(num) for _ in range(int(input())) for num in re.findall("\d+", input())
    ),
    sep="\n"
)
