import itertools
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
blanks = [(i, j) for i in range(N) for j in range(M) if data[i][j] == 0]
viruses = [(i, j) for i in range(N) for j in range(M) if data[i][j] == 2]
answer = -1

for new_walls in itertools.combinations(blanks, 3):
    test_data = [data[i][:] for i in range(N)]
    for (wall_i, wall_j) in new_walls:
        test_data[wall_i][wall_j] = 1

    # the viruses spread. (dfs)
    stack = viruses[:]
    visit = [[False] * M for _ in range(N)]

    while stack:
        i, j = stack.pop()
        if i < 0 or i >= N or j < 0 or j >= M or test_data[i][j] == 1 or visit[i][j]:
            continue
        visit[i][j] = True
        test_data[i][j] = 2
        stack.append((i + 1, j))
        stack.append((i - 1, j))
        stack.append((i, j + 1))
        stack.append((i, j - 1))

    answer = max(answer, sum(map(lambda x: x.count(0), test_data)))

print(answer)
