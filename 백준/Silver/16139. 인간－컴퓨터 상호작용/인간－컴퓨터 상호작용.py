import sys

input = sys.stdin.readline
S = input().rstrip()
q = int(input())

# counts[-1] is always 0 to prevent wrong indexing.
counts = {alpha: [0] * (len(S) + 1) for alpha in "abcdefghijklmnopqrstuvwxyz"}
for i, alpha in enumerate(S):
    counts[alpha][i] += 1

for alpha in counts.keys():
    # get the prefix-sum list of each alphabet.
    for i in range(1, len(S)):
        counts[alpha][i] += counts[alpha][i - 1]

for _ in range(q):
    alpha, l, r = input().split()
    print(counts[alpha][int(r)] - counts[alpha][int(l) - 1])
