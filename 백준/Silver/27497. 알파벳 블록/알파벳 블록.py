import sys
import collections

input = sys.stdin.readline
result = collections.deque()
trace = []  # 0 if front else -1

for _ in range(int(input())):
    cmd, *alpha = input().split()
    if cmd == "1":
        result.append(alpha[0])
        trace.append(-1)
    elif cmd == "2":
        result.appendleft(alpha[0])
        trace.append(0)
    elif trace:
        latest = trace.pop()
        if latest == 0:
            result.popleft()
        else:
            result.pop()

print("".join(result) if result else 0)
