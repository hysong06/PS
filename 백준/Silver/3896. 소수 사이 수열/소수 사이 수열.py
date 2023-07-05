import bisect
import sys

sieve = [True] * (1299709 + 1)

sieve[0] = sieve[1] = False
for i in range(2, len(sieve)):
    if sieve[i]:
        for k in range(i * i, len(sieve), i):
            sieve[k] = False

primes = [i for i in range(2, len(sieve)) if sieve[i]]


# main
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())

    if sieve[k]:
        print(0)
    else:
        idx = bisect.bisect(primes, k)
        print(primes[idx] - primes[idx - 1])
