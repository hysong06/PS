import sys

input = sys.stdin.readline
N = int(input())
data = list(enumerate(map(int, input().split()), start=1))
count = [0] * (N + 1)
nearest = [float("inf")] * (N + 1)


def solution(buildings):
    visibles = []  # stack

    for idx, height in buildings:
        while visibles and visibles[-1][1] <= height:
            visibles.pop()

        count[idx] += len(visibles)
        if visibles and abs(visibles[-1][0] - idx) < abs(nearest[idx] - idx):
            nearest[idx] = visibles[-1][0]

        visibles.append((idx, height))


# main
solution(data[:])
solution(data[::-1])

for c, n in zip(count[1:], nearest[1:]):
    if c == 0:
        print(c)
    else:
        print(c, n)
