import sys

input = sys.stdin.readline
odds = [num for num in [int(input()) for _ in range(7)] if num % 2 == 1]

if odds:
    print(sum(odds))
    print(min(odds))
else:
    print(-1)
