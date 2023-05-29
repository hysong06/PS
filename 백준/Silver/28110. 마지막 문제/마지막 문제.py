import sys

input = sys.stdin.readline
N = int(input())
difficulties = sorted(map(int, input().split()))


def solution():
    answer = -1
    max_diff = 0

    for i in range(N - 1):
        a, b = difficulties[i], difficulties[i + 1]
        mid = (a + b) // 2
        diff = mid - a

        if diff == 0:
            continue
        if diff > max_diff:
            answer, max_diff = mid, diff

    return answer


print(solution())
