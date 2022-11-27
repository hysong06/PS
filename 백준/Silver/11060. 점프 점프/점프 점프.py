import sys

input = sys.stdin.readline
N = int(input())
maze = list(map(int, input().split()))
jumps = [float("inf")] * N  # dp

jumps[0] = 0
for cur in range(N - 1):
    for step in range(1, maze[cur] + 1):
        nxt = cur + step
        if nxt < N:
            jumps[nxt] = min(jumps[cur] + 1, jumps[nxt])

print(jumps[-1] if jumps[-1] != float("inf") else -1)
