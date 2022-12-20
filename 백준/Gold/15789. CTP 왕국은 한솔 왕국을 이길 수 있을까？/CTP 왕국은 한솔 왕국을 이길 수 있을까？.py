import collections
import sys

sys.setrecursionlimit(200_001)
input = sys.stdin.readline
N, M = map(int, input().split())
allies = collections.defaultdict(set)
for _ in range(M):
    X, Y = map(int, input().split())
    allies[X].add(Y)
    allies[Y].add(X)
C, H, K = map(int, input().split())
visit = [False] * (N + 1)


def get_group_size(country: int) -> int:
    if visit[country]:
        return 0
    visit[country] = True
    return 1 + sum(get_group_size(ally) for ally in allies[country] if not visit[ally])


get_group_size(H)  # just visit check of the allies of Hansol's kingdom.
print(
    get_group_size(C)
    + sum(
        sorted(
            [get_group_size(i) for i in range(1, N + 1) if not visit[i]], reverse=True
        )[:K]
    )
)
