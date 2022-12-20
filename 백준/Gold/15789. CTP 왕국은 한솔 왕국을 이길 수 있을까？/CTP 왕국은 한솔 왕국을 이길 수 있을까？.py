import collections
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
allies = collections.defaultdict(set)
for _ in range(M):
    X, Y = map(int, input().split())
    allies[X].add(Y)
    allies[Y].add(X)
C, H, K = map(int, input().split())
visit = [False] * (N + 1)


def get_group_size(start: int) -> int:
    queue = collections.deque(iterable=[start])
    visit[start] = True
    group_size = 1

    while queue:  # bfs
        cur = queue.pop()
        for link in allies[cur]:
            if not visit[link]:
                queue.append(link)
                visit[link] = True
                group_size += 1

    return group_size


get_group_size(H)  # just visit check of the allies of Hansol's kingdom.
print(
    get_group_size(C)
    + sum(
        sorted(
            [get_group_size(i) for i in range(1, N + 1) if not visit[i]], reverse=True
        )[:K]
    )
)
