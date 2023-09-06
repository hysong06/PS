import sys
import heapq

input = sys.stdin.readline
heap = [int(input()) for _ in range(int(input()))]
heapq.heapify(heap)
compare = 0

while len(heap) > 1:
    merged = heapq.heappop(heap) + heapq.heappop(heap)
    compare += merged
    heapq.heappush(heap, merged)

print(compare)
