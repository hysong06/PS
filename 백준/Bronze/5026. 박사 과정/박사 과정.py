import sys

input = sys.stdin.readline
for _ in range(int(input())):
    problem = input().rstrip()
    print("skipped" if problem == "P=NP" else sum(map(int, problem.split("+"))))
