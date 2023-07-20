import sys

input = sys.stdin.readline
N, M = map(int, input().split())
basket = [0] * (N + 1)

for _ in range(M):
    i, j, k = map(int, input().split())
    basket[i : j + 1] = [k] * (j - i + 1)

print(*basket[1:])
