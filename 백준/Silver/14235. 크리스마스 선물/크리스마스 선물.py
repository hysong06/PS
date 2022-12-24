import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = [1] * n

for _ in range(n):
    a, *values = map(int, input().split())
    if a == 0:
        print(-heapq.heappop(heap))
        continue

    for value in values:
        heapq.heappush(heap, -value)
