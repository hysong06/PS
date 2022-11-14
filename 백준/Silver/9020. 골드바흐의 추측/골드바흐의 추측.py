import sys

input = sys.stdin.readline

# make the sieve of Eratosthenes.
sieve = [False, False] + [True] * (10000 - 1)
for i in range(2, 100 + 1):
    if sieve[i]:
        for k in range(i * i, 10000 + 1, i):
            sieve[k] = False

# solution here.
for _ in range(int(input())):
    n = int(input())
    left = right = n // 2

    while left > 1:
        if sieve[left] and sieve[right]:
            print(left, right)
            break
        left -= 1
        right += 1
