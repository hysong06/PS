import sys

input = sys.stdin.readline
N, M = map(int, input().split())
heights = list(map(int, input().split()))

variance = [0] * (N + 1)
for _ in range(M):
    a, b, k = map(int, input().split())
    variance[a - 1] += k
    variance[b] -= k

for i in range(1, len(variance)):
    variance[i] += variance[i - 1]  # prefix-sum

print(*map(sum, zip(heights, variance[:-1])))
