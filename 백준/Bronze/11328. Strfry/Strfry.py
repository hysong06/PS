import collections
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().split()
    print(
        "Possible" if collections.Counter(a) == collections.Counter(b) else "Impossible"
    )
