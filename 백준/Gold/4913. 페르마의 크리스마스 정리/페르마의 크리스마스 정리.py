import sys

max_U = 1_000_000  # not a prime number

"""
implement the sieve of Eratosthenes.
"""
is_prime = [True] * (max_U + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(len(is_prime) ** 0.5)):
    if is_prime[i]:
        for k in range(i * i, len(is_prime), i):
            is_prime[k] = False

"""
implement prefix-sum lists.
1) 'targets' are primes that is expressible as a**2 + b**2.
2) count_primes[0] and count_targets[0] is used as a border to negatives.
"""
count_primes = [0] * (max_U + 1)
count_targets = [0] * (max_U + 1)

# 2 is a 'target' because 2 == 1**1 + 1**1.
count_primes[2] = count_targets[2] = 1
for i in range(3, max_U + 1):
    count_primes[i] = count_primes[i - 1] + int(is_prime[i])
    count_targets[i] = count_targets[i - 1] + (1 if is_prime[i] and i % 4 == 1 else 0)

# main
input = sys.stdin.readline
while True:
    L, U = map(int, input().split())
    if L == U == -1:
        break
    x = count_primes[max(0, U)] - count_primes[max(0, L - 1)]
    y = count_targets[max(0, U)] - count_targets[max(0, L - 1)]
    print(L, U, x, y)
