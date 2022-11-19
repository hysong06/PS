import math
import sys

input = sys.stdin.readline
N = int(input())
rings = list(map(int, input().split()))

for cur_ring in rings[1:]:
    gcd = math.gcd(rings[0], cur_ring)
    print(f"{rings[0] // gcd}/{cur_ring // gcd}")
