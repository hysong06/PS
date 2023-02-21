import sys

input = sys.stdin.readline
head, tail = [], []
latest = []  # 0 if front else -1

for i in range(int(input())):
    cmd, *alpha = input().split()

    # add a new block.
    if cmd == "1":
        tail.append(alpha[0])
        latest.append(-1)
    elif cmd == "2":
        head.append(alpha[0])
        latest.append(0)

    # remove the latest-added block.
    elif latest:
        head.pop() if latest.pop() == 0 else tail.pop()

print(("".join(head[::-1]) + "".join(tail)) or 0)
