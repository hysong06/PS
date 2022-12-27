import sys

lines = list(map(lambda x: x.rstrip("\n"), sys.stdin.readlines()))
print(sum(map(int, ("".join(lines)).split(","))))
