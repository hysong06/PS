import sys

input = sys.stdin.readline
n = int(input())
sequence = [int(input()) for _ in range(n)]

pushed = 1
stack = []
actions = []

for target in sequence:
    while pushed <= target:
        stack.append(pushed)
        actions += "+"
        pushed += 1

    if stack.pop() == target:
        actions += "-"
    else:
        print("NO")
        break
else:
    print("\n".join(actions))
