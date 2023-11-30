import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    choice = {k: v for k, v in enumerate(map(int, input().split()), start=1)}
    left = n

    # one-person teams
    for k, v in list(choice.items()):
        if k == v:
            left -= 1
            del choice[k]

    # and the others
    stack = [(i, {i: 1}) for i in choice]

    while stack:
        cur, order = stack.pop()
        if cur not in choice:
            continue

        nxt = choice[cur]
        del choice[cur]  # checked

        if nxt in order:
            left -= len(order) + 1 - order[nxt]  # get the size of cycle
        else:
            order[nxt] = len(order) + 1
            stack.append((nxt, order))

    print(left)
