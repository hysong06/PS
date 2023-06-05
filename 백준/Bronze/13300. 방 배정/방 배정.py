import sys

input = sys.stdin.readline
N, K = map(int, input().split())
students = [[0] * 2 for _ in range(6)]
for _ in range(N):
    S, Y = map(int, input().split())
    students[Y - 1][S] += 1

print(
    sum(
        (students[year][sex] // K) + (0 if students[year][sex] % K == 0 else 1)
        for year in range(6)
        for sex in range(2)
    )
)
