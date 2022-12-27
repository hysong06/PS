import sys

S = "".join(map(lambda x: x.rstrip(), sys.stdin.readlines()))
print(sum(map(int, S.split(","))))
