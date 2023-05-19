import sys

input = sys.stdin.readline
N = int(input())
heights = list(map(int, input().split()))
count = 0
p = 0

while p < len(heights):
    count += 1

    i, j = p, p + 1
    while j < len(heights) and heights[i] > heights[j]:
        i, j = i + 1, j + 1

    p = j

print(count)
