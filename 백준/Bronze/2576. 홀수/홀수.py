import sys

input = sys.stdin.readline
sum_odds = 0
min_odds = 100

for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        sum_odds += num
        min_odds = min(num, min_odds)

if sum_odds == 0:
    print(-1)
else:
    print(sum_odds)
    print(min_odds)
