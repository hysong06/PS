import itertools
import sys

_, M, *elements = sys.stdin.read().split()
M = int(M)
elements = sorted(set(map(int, elements)))

*itertools.starmap(
    print,
    sorted(set(itertools.combinations_with_replacement(elements, M))),
),
