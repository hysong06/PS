import sys

while True:
    k, *S = map(int, sys.stdin.readline().split())
    if k == 0:
        break
    stack = []

    def solve(depth, cur):
        if depth == 6:
            print(*stack)
            return

        for nxt in range(cur + 1, k):
            stack.append(S[nxt])
            solve(depth + 1, nxt)
            stack.pop()

    solve(0, -1)
    print()
