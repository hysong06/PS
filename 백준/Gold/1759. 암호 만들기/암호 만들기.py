import itertools
import sys

input = sys.stdin.readline
L, C = map(int, input().split())
cons, vows = [], []
results = []

for char in input().split():
    if char in "aeiou":
        vows.append(char)
    else:
        cons.append(char)

for cons_count in range(2, L):
    vows_count = L - cons_count
    if vows_count > len(vows):
        continue

    for cons_comb in itertools.combinations(cons, cons_count):
        for vows_comb in itertools.combinations(vows, vows_count):
            results.append(sorted(cons_comb + vows_comb))

results.sort()
for result in results:
    print("".join(result))
