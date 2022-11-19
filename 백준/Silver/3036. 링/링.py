import sys

input = sys.stdin.readline
N = int(input())
rings = list(map(int, input().split()))


def get_fraction(a, b):
    A, B = a, b
    for i in range(min(A, B), 1, -1):
        if A % i == 0 and B % i == 0:
            A //= i
            B //= i
    return f"{A}/{B}"


for cur_ring in rings[1:]:
    print(get_fraction(rings[0], cur_ring))
