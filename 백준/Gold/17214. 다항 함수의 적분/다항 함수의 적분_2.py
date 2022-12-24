import re
import sys


def solution(expr: str) -> str:
    if expr == "0":
        return "W"

    def integral(term: str) -> str:
        if term.isdigit():
            return ("" if term == "1" else term) + "x"
        else:
            c = term[:-1]  # coefficient
            return ("" if c == "2" else str(int(c) // 2)) + "xx"

    result = ""
    if expr[0] == "-":
        result += expr[0]
        expr = expr[1:]

    terms = re.split("[+-]", expr)
    operators = [e for e in expr if e == "+" or e == "-"]

    for term, oper in zip(terms[:-1], operators):
        result += integral(term)
        result += oper
    return result + integral(terms[-1]) + "+W"


print(solution(sys.stdin.readline().rstrip("\n")))
