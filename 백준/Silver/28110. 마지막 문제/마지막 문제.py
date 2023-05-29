import sys

input = sys.stdin.readline
N = int(input())
difficulties = sorted(map(int, input().split()))


def solution():
    answer = -1
    max_diff = 0

    for a, b in zip(difficulties[:-1], difficulties[1:]):
        if b - a == 1:
            continue

        mid = (a + b) // 2
        diff = mid - a

        if diff > max_diff:
            answer, max_diff = mid, diff

    return answer


print(solution())
