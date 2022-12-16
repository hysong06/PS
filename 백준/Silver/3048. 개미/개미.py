import sys

input = sys.stdin.readline
N1, N2 = map(int, input().split())
group1 = input().rstrip("\n")
group2 = input().rstrip("\n")
T = int(input())
order = list(group1[::-1] + group2)

# solution
for _ in range(T):
    i = 0
    while i < len(order) - 1:
        if order[i] in group1 and order[i + 1] in group2:
            order[i], order[i + 1] = order[i + 1], order[i]
            i += 1
        i += 1

print("".join(order))
