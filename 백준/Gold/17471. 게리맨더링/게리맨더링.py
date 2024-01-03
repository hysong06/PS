import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
N = int(input())
populations = [0, *map(int, input().split())]
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    _, *graph[i] = map(int, input().split())


def is_connected(ward):
    queue = deque([ward.pop()])
    visit = {queue[0]}

    while queue:  # bfs
        cur = queue.popleft()
        for nxt in graph[cur]:
            if nxt not in ward or nxt in visit:
                continue
            ward.remove(nxt)
            visit.add(nxt)
            queue.append(nxt)

    return len(ward) == 0


def get_diff(A, B):
    if is_connected(A.copy()) and is_connected(B.copy()):
        return abs(sum(populations[a] for a in A) - sum(populations[b] for b in B))
    return sys.maxsize


# main
src = set(range(1, N + 1))
isolated = graph.count([]) - 1  # except graph[0]

if isolated > 1:
    print(abs(populations[1] - populations[2]) if N == 2 else -1)

elif isolated == 1:
    A = {graph.index([], 1)}
    print(get_diff(A, src - A))

else:
    print(
        min(
            get_diff(set(A), src - set(A))
            for i in range(1, N // 2 + 1)
            for A in combinations(src, i)
        )
    )
