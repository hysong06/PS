import sys

N = int(sys.stdin.readline())
count = 0

for number in range(2023, N + 1):
    number = str(number)
    if number.count("2") < 2 or "0" not in number or "3" not in number:
        continue

    # search() return "" if target not in source.
    def search(source, target):
        result = source[source.find(target) + 1 :]
        return "" if len(source) == len(result) else result

    if len(search(search(search(search(number + "#", "2"), "0"), "2"), "3")) > 0:
        count += 1

print(count)
