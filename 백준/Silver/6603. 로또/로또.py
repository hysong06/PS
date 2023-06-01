import sys

while True:
    k, *S = sys.stdin.readline().split()
    if k == "0":
        break
    stack = []

    def solve(depth, cur):
        if depth == 6:
            print(" ".join(stack))
            return

        for nxt in range(cur + 1, len(S) - (6 - depth) + 1):
            stack.append(S[nxt])
            solve(depth + 1, nxt)
            stack.pop()

    solve(0, -1)
    print()
