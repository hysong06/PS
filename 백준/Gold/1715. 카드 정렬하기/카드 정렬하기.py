import sys
import heapq

input = sys.stdin.readline
heap = [int(input()) for _ in range(int(input()))]
heapq.heapify(heap)

count = 0
while len(heap) > 1:
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    count += num1 + num2
    heapq.heappush(heap, num1 + num2)
print(count)
