import itertools
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
array = map(int, input().split())

*itertools.starmap(
    print,
    sorted(set(itertools.combinations_with_replacement(sorted(array), M))),
),
