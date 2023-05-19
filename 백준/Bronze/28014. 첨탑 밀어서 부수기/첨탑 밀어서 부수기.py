import sys

input = sys.stdin.readline
N = int(input())
heights = list(map(int, input().split()))
count = 0
p = 0

while p < len(heights):
    count += 1

    i = p
    while i < len(heights) - 1 and heights[i] > heights[i + 1]:
        i += 1
    p = i + 1

print(count)
