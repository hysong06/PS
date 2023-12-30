N = int(input())
columns = [0] * N  # whether 'j' is promising or not
right_diagonals = [0] * (2 * N)  # whether 'i + j' is promising or not
left_diagonals = [0] * (3 * N)  # whether 'i - j' is promising or not
count = 0


def queen(i, j, value):
    columns[j] += value
    right_diagonals[i + j] += value
    left_diagonals[i - j] += value


def solve(i):
    global count
    if i == N:
        count += 1
        return

    for j in range(N):
        if columns[j] == right_diagonals[i + j] == left_diagonals[i - j] == 0:
            queen(i, j, 1)
            solve(i + 1)
            queen(i, j, -1)


solve(0)
print(count)
