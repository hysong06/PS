import bisect
import sys

input = sys.stdin.readline
scores = [int(input()) for _ in range(10)]
for i in range(1, 10):
    scores[i] += scores[i - 1]

idx = max(1, min(bisect.bisect_left(scores, 100), 9))
print(
    scores[idx - 1]
    if abs(scores[idx - 1] - 100) < abs(scores[idx] - 100)
    else scores[idx]
)
