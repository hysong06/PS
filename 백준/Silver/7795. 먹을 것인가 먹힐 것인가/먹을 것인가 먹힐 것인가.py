import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()), reverse=True)
    B = sorted(map(int, input().split()), reverse=True)
    i, count = 0, 0

    for a in A:
        while i < M and B[i] >= a:
            i += 1
        count += M - i

    print(count)
