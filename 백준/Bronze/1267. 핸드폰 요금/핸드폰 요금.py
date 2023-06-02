import sys

input = sys.stdin.readline
input()
calls = list(map(int, input().split()))
ys = sum(map(lambda x: 10 * (x // 30 + 1), calls))
ms = sum(map(lambda x: 15 * (x // 60 + 1), calls))

if ys < ms:
    print("Y", ys)
elif ys > ms:
    print("M", ms)
else:
    print("Y M", ys)
