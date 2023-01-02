import itertools
import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

print(
    max(
        sum(abs(order[i] - order[i - 1]) for i in range(N - 1))
        for order in itertools.permutations(A, N)
    )
)
