import sys

cards = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, sys.stdin.readline().split())
    cards[a - 1 : b] = cards[a - 1 : b][::-1]

print(*cards)
