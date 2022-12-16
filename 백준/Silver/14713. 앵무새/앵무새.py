import collections
import sys

input = sys.stdin.readline
N = int(input())
S = [collections.deque(iterable=input().split()) for _ in range(N)]
L = collections.deque(iterable=input().split())


def solution() -> str:
    while L:
        for sentence in S:
            if sentence and sentence[0] == L[0]:
                sentence.popleft()
                L.popleft()
                break
        else:  # if there is no L[0] in any sentences
            return "Impossible"

    for sentence in S:  # if not all sentences are written
        if sentence:
            return "Impossible"

    return "Possible"


print(solution())
