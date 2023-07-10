import itertools
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    mbtis = input().split()

    if N > 32:  # pigeonhole principle
        print(0)
        continue

    print(
        min(
            sum(
                int(a[i] != b[i]) + int(b[i] != c[i]) + int(c[i] != a[i])
                for i in range(4)
            )
            for a, b, c in itertools.combinations(mbtis, 3)
        )
    )
