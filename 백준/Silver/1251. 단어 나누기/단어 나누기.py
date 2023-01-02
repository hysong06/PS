import sys

input = sys.stdin.readline
word = input().rstrip("\n")
results = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        a, b, c = word[:i], word[i:j], word[j:]
        results.append(a[::-1] + b[::-1] + c[::-1])

print(sorted(results)[0])
