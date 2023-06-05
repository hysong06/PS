import collections

counter = collections.Counter(input())

answer = (counter["6"] + counter["9"] + 1) // 2
counter["6"] = counter["9"] = 0
answer = max(answer, max(counter.values()))

print(answer)
