import sys

input = sys.stdin.readline
scores = dict()

for _ in range(int(input())):
    name, kor, eng, math = input().split()
    scores[name] = (int(kor), int(eng), int(math))

print(
    "\n".join(
        sorted(
            scores.keys(), key=lambda x: (-scores[x][0], scores[x][1], -scores[x][2], x)
        )
    )
)
