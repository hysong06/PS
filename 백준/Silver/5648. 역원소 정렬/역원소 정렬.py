import sys

print(*sorted(map(lambda x: int(x[::-1]), sys.stdin.read().split()[1:])), sep="\n")
