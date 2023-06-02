import sys

input = sys.stdin.readline
A, B = sorted(map(int, input().split()))
r = range(A + 1, B)

print(len(r))
print(*r)
