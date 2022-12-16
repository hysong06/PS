import collections
import sys

input = sys.stdin.readline
N = int(input())
S = [collections.deque(iterable=input().split()) for _ in range(N)]
L = input().split()


def solution() -> str:
    for finding in L:
        for sentence in S:
            if sentence and sentence[0] == finding:
                sentence.popleft()
                break
        else:  # if there is no 'finding' in any sentences
            return "Impossible"

    for sentence in S:  # if not all words are written
        if sentence:
            return "Impossible"

    return "Possible"


print(solution())
