N = int(input())
lines = [" " * (N - 1 - i) + "*" * (2 * i + 1) for i in range(N)]
print("\n".join(lines + lines[-2::-1]))
