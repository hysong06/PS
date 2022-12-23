import collections
import sys

input = sys.stdin.readline
S = input().rstrip("\n")
q = int(input())

# counts[-1] is always 0 to prevent wrong indexing.
counts = collections.defaultdict(lambda: [0] * (len(S) + 1))
for i, alpha in enumerate(S):
    counts[alpha][i] += 1

for count in counts.values():
    # make the prefix-sum list of each alphabet in S.
    for i in range(1, len(S)):
        count[i] += count[i - 1]

for _ in range(q):
    alpha, l, r = input().split()
    l, r = int(l), int(r)
    print(counts[alpha][r] - counts[alpha][l - 1])
