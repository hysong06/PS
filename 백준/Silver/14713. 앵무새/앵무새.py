import collections
import sys

input = sys.stdin.readline
N = int(input())
S = [collections.deque(iterable=input().split()) for _ in range(N)]
L = collections.deque(iterable=input().split())


def solution() -> str:
    while L:
        prev_len = len(L)
        for i in range(N):
            while S[i] and L and S[i][0] == L[0]:
                S[i].popleft()
                L.popleft()
        if prev_len == len(L):
            return "Impossible"

    for q in S:
        if q:
            return "Impossible"
    return "Possible"


print(solution())
