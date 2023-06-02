import sys

for _ in range(3):
    print("EABCD"[(sys.stdin.readline().split()).count("0")])
