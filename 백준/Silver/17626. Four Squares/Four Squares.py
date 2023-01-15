def solution(n: int) -> int:
    sqrt_n = int(n**0.5)

    if n == sqrt_n**2:
        return 1

    for a in range(1, sqrt_n + 1):
        b = int((n - a**2) ** 0.5)
        if n == a**2 + b**2:
            return 2

    for a in range(1, sqrt_n + 1):
        for b in range(a, int((n - a**2) ** 0.5) + 1):
            c = int((n - a**2 - b**2) ** 0.5)
            if n == a**2 + b**2 + c**2:
                return 3

    return 4


print(solution(int(input())))
