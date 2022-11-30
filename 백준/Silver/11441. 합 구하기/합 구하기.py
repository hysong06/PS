import sys

input = sys.stdin.readline
N = int(input())
psum = [0] + list(map(int, input().split()))
for i in range(2, N + 1):
    psum[i] += psum[i - 1]

for _ in range(int(input())):
    i, j = map(int, input().split())
    print(psum[j] - psum[i - 1])
