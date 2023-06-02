import sys

input = sys.stdin.readline
A, B = map(int, input().split())
if A == B:
    print(0)
    print()
    exit(0)

A, B = min(A, B), max(A, B)
print(B - A - 1)
print(*[i for i in range(A + 1, B)])
