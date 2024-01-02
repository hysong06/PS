import sys

input = sys.stdin.readline

for _ in range(int(input())):
    num = int(input())

    for base in range(2, int(num**0.5) + 1):
        exp = 0
        while num % base == 0:
            num //= base
            exp += 1

        if exp:
            print(base, exp)

    # if num is prime itself
    if num > 1:
        print(num, 1)
