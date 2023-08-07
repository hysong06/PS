import sys

input = sys.stdin.readline
N = int(input())
S = [input().rstrip() for _ in range(N)]
M = int(input())
A = [input().rstrip() for _ in range(M)]

idx = S.index("?")
head = {*"abcdefghijklmnopqrstuvwxyz"} if idx == 0 else {S[idx - 1][-1]}
tail = {*"abcdefghijklmnopqrstuvwxyz"} if idx == N - 1 else {S[idx + 1][0]}

for a in A:
    if a not in S and a[0] in head and a[-1] in tail:
        print(a)
        break
