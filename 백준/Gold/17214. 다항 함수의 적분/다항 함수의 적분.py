import sys


def integral(expr: str) -> str:
    if expr == "0":
        return "W"

    result = ""
    l, r = 0, int(expr[0] == "-")

    while r < len(expr):
        # 1. expr.split("+" or "-") to find a signed-term.
        while r < len(expr) and expr[r] != "+" and expr[r] != "-":
            r += 1

        # 2. process the signs.
        if expr[l] == "+" or expr[l] == "-":
            result += expr[l]
            l += 1

        # 3. process the term.
        term = expr[l:r]
        if term.isdigit():
            result += "x" if term == "1" else term + "x"
        else:
            c = term[:-1]
            result += "xx" if c == "2" else str(int(c) // 2) + "xx"

        # 4. find the next term if exist.
        l = r
        r = l + 1

    return result + "+W"


print(integral(sys.stdin.readline().rstrip("\n")))
