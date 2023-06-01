import sys

input = sys.stdin.readline
N, S = map(int, input().split())
nums = list(map(int, input().split()))
count = 0


def solve(total, i):
    global count
    if i == N:
        if total == S:
            count += 1
        return
    solve(total, i + 1)
    solve(total + nums[i], i + 1)


solve(0, 0)
if S == 0:
    count -= 1  # except the subsequence of which length is zero.
print(count)
