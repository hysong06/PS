import sys

input = sys.stdin.readline
odds = []

for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        odds.append(num)

if odds:
    print(sum(odds))
    print(min(odds))
else:
    print(-1)
