import heapq
import sys

input = sys.stdin.readline
N, L = map(int, input().split())
A = list(map(int, input().split()))
heap = []

for i, value in enumerate(A):
    while heap and heap[0][1] <= i - L:
        heapq.heappop(heap)

    heapq.heappush(heap, (value, i))

    A[i] = heap[0][0]  # reuse A

print(*A)
