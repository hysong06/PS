import sys

board = list(map(lambda x: list(x[::-1]), sys.stdin.read().split()))
result = ""
flag = True

while flag:
    flag = False

    for stack in board:
        if not stack:
            continue
        result += stack.pop()
        flag = True

print(result)
