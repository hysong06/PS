import sys

input = sys.stdin.readline
index_of = dict()

for _ in range(int(input())):
    a, b, *c = map(int, input().split())

    if c:  # 1 x w
        index_of[c[0]] = b
    else:  # 2 w
        print(index_of[b])
