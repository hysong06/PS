import sys

# the sieve of Eratosthenes
is_prime = [False, False] + [True] * 99999

for i in range(2, int(len(is_prime) ** 0.5) + 1):
    if not is_prime[i]:
        continue
    for k in range(i * i, len(is_prime), i):
        is_prime[k] = False

# main
input = sys.stdin.readline

for _ in range(int(input())):
    num = int(input())

    for base in range(2, num + 1):
        if is_prime[base] and num % base == 0:
            exp = 0
            while num % base == 0:
                num //= base
                exp += 1
            print(base, exp)
