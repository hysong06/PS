import sys

input = sys.stdin.readline
N, K = map(int, input().split())
R, C = map(int, input().split())  # king
attacked_row = set()
attacked_col = set()
attacked_diag1 = set()
attacked_diag2 = set()

for _ in range(K):  # queens
    r, c = map(int, input().split())
    attacked_row.add(r)
    attacked_col.add(c)
    attacked_diag1.add(r + c)
    attacked_diag2.add(r - c)


def attacked(i: int, j: int) -> bool:
    if (
        i in attacked_row
        or j in attacked_col
        or i + j in attacked_diag1
        or i - j in attacked_diag2
    ):
        return True
    return False


def evitable() -> bool:
    delta = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))
    for (dr, dc) in delta:
        nr, nc = R + dr, C + dc
        if 1 <= nr <= N and 1 <= nc <= N and not attacked(nr, nc):
            return True
    return False


# main
if attacked(R, C):
    if evitable():
        print("CHECK")
    else:
        print("CHECKMATE")
elif not evitable():
    print("STALEMATE")
else:
    print("NONE")
