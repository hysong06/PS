import sys

N = sys.stdin.readline().rstrip()
N, len_N = int(N), len(N)
i, len_i = 1, 1
result = 0

while len_i < len_N:
    result += len_i * (10 * i - i)
    i, len_i = i * 10, len_i + 1

result += len_i * (N - i + 1)

print(result)
