from itertools import combinations
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(N)]

print(
    max(
        sum(C[i][j] for i, j in combinations(ingredients, 2))
        for ingredients in combinations(range(N), K)
    )
)
