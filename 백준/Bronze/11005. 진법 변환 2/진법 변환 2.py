import sys

input = sys.stdin.readline
N, B = map(int, input().split())
to_char = {v: ch for v, ch in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
stack = ""

while N != 0:
    stack += to_char[N % B]
    N //= B

print(stack[::-1])
