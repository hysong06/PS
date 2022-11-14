import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    seen = set(map(int, input().split()))
    M = int(input())
    tests = list(map(int, input().split()))

    for test in tests:
        print(1 if test in seen else 0)
