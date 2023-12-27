from collections import deque
import sys

MAX = 50
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]

while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)


def get_score(start):
    queue = deque()
    visit = [False] * (n + 1)
    count = 0
    score = 0

    def check(i):
        nonlocal count
        queue.append(i)
        visit[i] = True
        count += 1

    check(start)

    while count < n:
        score += 1

        for _ in range(len(queue)):
            member = queue.popleft()
            for friend in graph[member]:
                if not visit[friend]:
                    check(friend)

            if count == n:
                return score


scores = [MAX, *(get_score(i) for i in range(1, n + 1))]
min_score = min(scores)
print(min_score, scores.count(min_score))
print(*(i for i in range(1, n + 1) if scores[i] == min_score))
