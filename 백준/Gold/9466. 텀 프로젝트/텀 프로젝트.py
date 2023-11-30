import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    prefer = {s: t for s, t in enumerate(map(int, input().split()), start=1)}

    # dfs, return the size of cycle
    def find_cycle(student, order):
        if student not in prefer:  # if already checked
            return 0
        choice = prefer[student]
        del prefer[student]  # check

        if choice in order:
            return len(order) + 1 - order[choice]
        else:
            order[choice] = len(order) + 1
            return find_cycle(choice, order)

    print(n - sum(find_cycle(i, {i: 1}) for i in range(1, n + 1)))
