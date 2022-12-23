import sys

input = sys.stdin.readline
input()  # N
S = input().rstrip("\n")

print(min(S.count(char) for char in "HIARC"))
