import sys

input = sys.stdin.readline
count_belly = ["E", "A", "B", "C", "D"]

for _ in range(3):
    print(count_belly[(input().split()).count("0")])
