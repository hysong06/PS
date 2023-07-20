import sys

input = sys.stdin.readline
to_score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}
a = 0.0
b = 0

for _ in range(20):
    _, credit, grade = input().split()
    if grade == "P":
        continue

    a += to_score[grade] * float(credit)
    b += int(credit[0])

print(a / b)
