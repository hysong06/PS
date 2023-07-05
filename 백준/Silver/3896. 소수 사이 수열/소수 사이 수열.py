import bisect
import sys

# the sieve of Eratosthenes
max_k = 1299709
primes = set(range(2, max_k + 1))

for i in range(2, max_k + 1):
    if i in primes:
        primes -= set(range(i * i, max_k + 1, i))

sorted_primes = sorted(primes)


# main
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())

    if k in primes:
        print(0)
        continue

    idx = bisect.bisect(sorted_primes, k)
    print(sorted_primes[idx] - sorted_primes[idx - 1])
