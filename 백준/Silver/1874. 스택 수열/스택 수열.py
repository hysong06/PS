import sys

input = sys.stdin.readline
pushed = 1
stack = []
actions = []

for _ in range(int(input())):
    target = int(input())

    while pushed <= target:
        stack.append(pushed)
        actions += "+"
        pushed += 1

    if stack[-1] == target:
        stack.pop()
        actions += "-"

print("NO" if stack else "\n".join(actions))
