import sys

input = sys.stdin.readline
N = int(input())
group = set()

for _ in range(N):
    group.add("".join(sorted(input().rstrip())))
print(len(group))
