import collections
import sys

input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
queue = collections.deque([(S, 0)])
visit = [False] * (F + 1)

# bfs
while queue:
    floor, depth = queue.popleft()
    if floor < 1 or floor > F or visit[floor]:
        continue
    if floor == G:
        print(depth)  # if possible
        break
    visit[floor] = True
    queue.append((floor + U, depth + 1))
    queue.append((floor - D, depth + 1))
else:
    print("use the stairs")  # if impossible
