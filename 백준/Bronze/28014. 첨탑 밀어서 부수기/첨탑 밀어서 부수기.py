input()
count = 0  # must push the first tower
prev = 0

for cur in map(int, input().split()):
    if prev <= cur:
        count += 1
    prev = cur

print(count)
