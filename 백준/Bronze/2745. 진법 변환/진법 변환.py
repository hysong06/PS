import sys

input = sys.stdin.readline
N, B = input().split()
B = int(B)
to_value = {ch: v for v, ch in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

print(sum(to_value[ch] * (B**i) for i, ch in enumerate(N[::-1])))
