import sys

input = sys.stdin.readline
n, m = map(int, input().split(":"))

for i in range(min(n, m) + 1, 1, -1):
    if n % i == m % i == 0:
        n //= i
        m //= i

print(f"{n}:{m}")
