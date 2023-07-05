import bisect
import sys

# the sieve of Eratosthenes
is_prime = [True] * (1299709 + 1)

is_prime[0] = is_prime[1] = False
for i in range(2, len(is_prime)):
    if is_prime[i]:
        for k in range(i * i, len(is_prime), i):
            is_prime[k] = False

sorted_primes = [i for i in range(2, len(is_prime)) if is_prime[i]]


# main
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())

    if is_prime[k]:
        print(0)
        continue

    idx = bisect.bisect(sorted_primes, k)
    print(sorted_primes[idx] - sorted_primes[idx - 1])
