import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    a, *values = list(map(int, input().split()))
    if a == 0:
        print(-heapq.heappop(heap) if heap else -1)
        continue

    for value in values:
        heapq.heappush(heap, -value)
