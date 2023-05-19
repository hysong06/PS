import sys

input = sys.stdin.readline
N = int(input())
heights = list(map(int, input().split()))
push = 1  # must push the first tower

for i in range(len(heights) - 1):
    if heights[i] <= heights[i + 1]:
        push += 1

print(push)
