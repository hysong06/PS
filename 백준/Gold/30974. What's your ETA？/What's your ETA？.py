import sys
import heapq
from collections import defaultdict

# the sieve of Eratosthenes
prime = [False, False] + [True] * 9_999_999
for i in range(2, int(len(prime) ** 0.5) + 1):
    if prime[i]:
        for k in range(i * i, len(prime), i):
            prime[k] = False

# init
input = sys.stdin.readline
N, M = map(int, input().split())
code = [0, *map(int, input().split())]
graph = defaultdict(lambda: defaultdict(int))

for _ in range(M):
    u, v, w = map(int, input().split())
    if prime[code[u] + code[v]] and (not graph[u][v] or w < graph[u][v]):
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
