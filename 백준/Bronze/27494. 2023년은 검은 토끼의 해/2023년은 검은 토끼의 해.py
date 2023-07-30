import sys

N = int(sys.stdin.readline())
count = 0

for number in range(2023, N + 1):
    number = str(number)

    if number.count("2") < 2 or "0" not in number or "3" not in number:
        continue

    x = number[number.find("2") + 1 :]
    y = x[x.find("0") + 1 :]
    z = y[y.find("2") + 1 :]
    w = z[z.find("3") + 1 :]

    if len(x) > len(y) > len(z) > len(w):
        count += 1

print(count)
