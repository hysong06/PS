import sys

input = sys.stdin.readline
count = 0

for _ in range(int(input())):
    word = input().rstrip("\n")
    stack = []

    for ch in word:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    if not stack:
        count += 1

print(count)
