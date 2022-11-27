import heapq
import sys

input = sys.stdin.readline
N = int(input())
maze = list(map(int, input().split()))


def shortest_path() -> int:
    heap = [(0, 0)]
    visit = [True] + [False] * (N - 1)

    while heap:
        jumps, cur = heapq.heappop(heap)
        if cur == N - 1:
            return jumps
        for step in range(1, maze[cur] + 1):
            nxt = cur + step
            if nxt < N and not visit[nxt]:
                visit[nxt] = True
                heapq.heappush(heap, (jumps + 1, nxt))

    return -1


print(shortest_path())
