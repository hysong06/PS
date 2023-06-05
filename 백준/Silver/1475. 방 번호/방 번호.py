counter = [0] * 10
for i in input():
    counter[(int(i))] += 1

counter[6], counter[9] =\
    (counter[6] + counter[9]) // 2, (counter[6] + counter[9] + 1) // 2

print(max(counter))
