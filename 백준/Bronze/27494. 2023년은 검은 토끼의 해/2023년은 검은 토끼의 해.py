import sys

N = int(sys.stdin.readline())
count = 0

for number in range(2023, N + 1):
    number = str(number)

    if number.count("2") < 2 or "0" not in number or "3" not in number:
        continue

    def search(idx, target):
        while idx < len(number) and number[idx] != target:
            idx += 1
        return idx

    x = search(0, "2")
    y = search(x + 1, "0")
    z = search(y + 1, "2")
    w = search(z + 1, "3")

    if x < y < z < w < len(number):
        count += 1

print(count)
