import itertools
import sys

input = sys.stdin.readline
nums = map(int, input().split())
dest = int(input())

answers = sorted(set(c for c in itertools.combinations(nums, 2) if sum(c) == dest))
for answer in answers:
    print(*answer)
print(len(answers))
