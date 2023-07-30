import sys

N = sys.stdin.readline().rstrip()
N, len_N = int(N), len(N)
result = 0

for k in range(len_N):
    result += N - 10**k + 1

print(result)
