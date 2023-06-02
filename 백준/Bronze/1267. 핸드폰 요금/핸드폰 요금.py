import sys

input = sys.stdin.readline
input()
calls = list(map(int, input().split()))

ys = sum(10 * (call // 30 + 1) for call in calls)
ms = sum(15 * (call // 60 + 1) for call in calls)
print(f"Y M {ys}" if ys == ms else (f"Y {ys}" if ys < ms else f"M {ms}"))
