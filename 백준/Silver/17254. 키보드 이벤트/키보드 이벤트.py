import sys

input = sys.stdin.readline
N, M = map(int, input().split())
inputs = sorted((int((t := input().split())[1]), int(t[0]), t[2]) for _ in range(M))
print("".join(c for _, _, c in inputs))
