import collections
import sys

input = sys.stdin.readline

# make the sieve of Eratosthenes.
primes = set(range(2, 10000))
for i in range(2, 101):
    if i in primes:
        primes -= set(range(i * i, 10000, i))
primes -= set(range(2, 1000))
primes = set(map(str, primes))  # consider the passwords as string.


def solution() -> int:
    src, dest = input().split()
    queue = collections.deque([(src, 0)])
    visits = set()

    while queue:
        password, level = queue.popleft()
        digits = list(password)

        if password not in primes or password in visits:
            continue
        visits.add(password)
        if password == dest:
            return level  # possible

        for i in range(4):
            temp = digits[i]
            for num in range(10):
                digits[i] = str(num)
                queue.append(("".join(digits), level + 1))
            digits[i] = temp

    return -1  # impossible


# main
for _ in range(int(input())):
    result = solution()
    print("impossible" if result == -1 else result)
