import sys

input = sys.stdin.readline
n = int(input())
word = input().rstrip()
answer = 0

left = 0  # the start of hidden number
while left < n:
    if word[left].isalpha():
        left += 1
        continue

    right = left + 1  # the end of hidden number
    while right < n and word[right].isdigit():
        right += 1

    answer += int(word[left:right])

    left = right + 1

print(answer)
