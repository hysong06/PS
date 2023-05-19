import sys

input = sys.stdin.readline
input()
count = 0
prev = 0

for cur in map(int, input().split()):
    if prev <= cur:
        count += 1
    prev = cur

print(count)
