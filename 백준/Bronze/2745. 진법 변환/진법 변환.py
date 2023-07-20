import sys

input = sys.stdin.readline
N, B = input().split()
B = int(B)
to_value = {ch: v for v, ch in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

result = 0
unit = B ** (len(N) - 1)

for ch in N:
    result += to_value[ch] * unit
    unit //= B

print(result)
