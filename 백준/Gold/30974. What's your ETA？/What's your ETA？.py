import sys
import heapq
from collections import defaultdict

# the sieve of Eratosthenes
is_prime = [False, False] + [True] * 9_999_999
for i in range(2, int(len(is_prime) ** 0.5) + 1):
    if is_prime[i]:
        for k in range(i * i, len(is_prime), i):
            is_prime[k] = False

# init
input = sys.stdin.readline
N, M = map(int, input().split())
code = [0, *map(int, input().split())]
graph = [defaultdict(lambda: float("inf")) for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    if not is_prime[code[u] + code[v]]:
        continue
    w = min(graph[u][v], w)
    graph[u][v] = graph[v][u] = w

# Dijkstra's algorithm
heap = [(0, 1)]
visit = [False] * (N + 1)

while heap:
    times, u = heapq.heappop(heap)
    if u == N:
        print(times)
        break

    if visit[u]:
        continue
    visit[u] = True

    for v, w in graph[u].items():
        heapq.heappush(heap, (times + w, v))
else:
    print("Now where are you?")
