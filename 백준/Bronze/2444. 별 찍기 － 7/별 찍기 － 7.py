N = int(input())
lines = ["{}{}".format(" " * (N - 1 - i), "*" * (2 * i + 1)) for i in range(N)]
print(*(lines + lines[-2::-1]), sep="\n")
