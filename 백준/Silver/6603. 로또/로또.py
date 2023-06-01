import itertools
import sys

while True:
    k, *S = sys.stdin.readline().split()
    if k == "0":
        break

    for comb in itertools.combinations(S, 6):
        print(*comb)
    print()
