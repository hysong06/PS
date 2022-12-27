import math
import sys

input = sys.stdin.readline
n, m = map(int, input().split(":"))
k = math.gcd(n, m)
print(n // k, m // k, sep=":")
