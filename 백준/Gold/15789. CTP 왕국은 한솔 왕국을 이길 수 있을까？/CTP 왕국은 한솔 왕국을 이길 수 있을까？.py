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
    stack = [start]
    group_size = 0

    while stack:  # dfs
        cur = stack.pop()
        if visit[cur]:
            continue
        visit[cur] = True
        group_size += 1
        for link in allies[cur]:
            if not visit[link]:
                stack.append(link)

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
