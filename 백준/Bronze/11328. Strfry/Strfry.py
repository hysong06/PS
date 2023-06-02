import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().split()
    print("Possible" if sorted(a) == sorted(b) else "Impossible")
