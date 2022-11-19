import sys

input = sys.stdin.readline
N = int(input())
scores = dict()
names = []

for _ in range(N):
    name, kor, eng, math = input().split()
    scores[name] = (int(kor), int(eng), int(math))
    names.append(name)

names.sort(key=lambda x: (-scores[x][0], scores[x][1], -scores[x][2], x))
print("\n".join(names))
