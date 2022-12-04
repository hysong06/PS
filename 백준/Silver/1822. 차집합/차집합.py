import sys

input = sys.stdin.readline
len_A, len_B = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

diff = A - B
print(len(diff))
print(*sorted(diff), end="")
