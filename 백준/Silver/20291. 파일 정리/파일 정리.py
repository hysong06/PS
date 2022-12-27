import collections
import sys

input = sys.stdin.readline
N = int(input())
data = collections.defaultdict(int)
for _ in range(N):
    _, extension = input().rstrip("\n").split(".")
    data[extension] += 1

for k in sorted(data):
    print(k, data[k])
