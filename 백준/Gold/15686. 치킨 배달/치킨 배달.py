import itertools
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
houses = [(i, j) for i in range(N) for j in range(N) if city[i][j] == 1]
chickens = [(i, j) for i in range(N) for j in range(N) if city[i][j] == 2]
answer = sys.maxsize

for selected_chickens in itertools.combinations(chickens, M):
    dist_sum = 0  # == the chicken distance of the city.
    for house in houses:
        dist_sum += min(
            abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            for chicken in selected_chickens
        )
    answer = min(answer, dist_sum)

print(answer)
