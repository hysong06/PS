import bisect
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    T, *heights = map(int, input().split())
    line = [heights.pop(0)]
    steps = 0

    for cur in heights:
        idx = bisect.bisect(line, cur)
        steps += len(line) - idx
        line.insert(idx, cur)

    print(T, steps)
