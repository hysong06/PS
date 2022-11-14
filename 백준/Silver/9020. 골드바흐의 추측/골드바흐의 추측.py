import sys

sieve = set(range(10001))
for i in range(2, 100 + 1):
    if i in sieve:
        sieve -= set(range(i * i, 10000 + 1, i))

# main
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    left = right = n // 2

    while left > 1:
        if left in sieve and right in sieve:
            print(left, right)
            break
        left -= 1
        right += 1
        
