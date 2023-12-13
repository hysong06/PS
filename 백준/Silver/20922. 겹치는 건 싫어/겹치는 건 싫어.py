import sys

input = sys.stdin.readline
N, K = map(int, input().split())
array = [*map(int, input().split())]
counter = [0] * 100001
answer = 0

left = 0
for right, value in enumerate(array):
    counter[value] += 1

    if counter[value] > K:
        temp = array.index(value, left) + 1
        for i in range(left, temp):
            counter[array[i]] -= 1
        left = temp

    answer = max(right - left + 1, answer)

print(answer)
