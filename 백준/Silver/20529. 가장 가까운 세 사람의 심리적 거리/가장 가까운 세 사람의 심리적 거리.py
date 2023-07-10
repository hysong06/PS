import collections
import itertools
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    mbtis = input().split()

    if N > 32:  # pigeonhole principle
        print(0)
        continue

    min_dist = float("inf")

    for a, b, c in itertools.combinations(mbtis, 3):
        counter = collections.Counter(a + b + c)
        dist = (
            counter["E"] * counter["I"]
            + counter["S"] * counter["N"]
            + counter["T"] * counter["F"]
            + counter["J"] * counter["P"]
        )
        min_dist = min(dist, min_dist)

    print(min_dist)
