import sys

input = sys.stdin.readline
N = int(input())
heights = [int(input()) for _ in range(N)]
prevs = []
count = 0

for cur in heights:
    while prevs and prevs[-1] <= cur:
        prevs.pop()
    count += len(prevs)

    prevs.append(cur)

print(count)
