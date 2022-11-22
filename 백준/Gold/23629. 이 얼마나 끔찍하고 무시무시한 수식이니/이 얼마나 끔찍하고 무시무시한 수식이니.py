import collections
import sys

input = sys.stdin.readline
dic = {
    "0": "ZERO",
    "1": "ONE",
    "2": "TWO",
    "3": "THREE",
    "4": "FOUR",
    "5": "FIVE",
    "6": "SIX",
    "7": "SEVEN",
    "8": "EIGHT",
    "9": "NINE",
}
impossible = "Madness!"


def solution(string: str) -> tuple:
    operations = {"+", "-", "x", "/"}

    """
    for first answer:
        make a mathematical expression
        by replacing each word in string with number.
    """
    expr = string[:]
    for num, word in dic.items():
        expr = expr.replace(word, num)

    # check whether the expression is well-transformed.
    for e in expr:
        if e.isupper():
            return (impossible,)

    for i in range(len(expr) - 1):
        if (expr[i] in operations and expr[i + 1] in operations) or expr[i] == "=":
            return (impossible,)

    """
    for second answer:
        calculate the expression,
        and replace each number in it with word if possible.
    """
    deq = collections.deque()  # if expr == "123+456", deq == [123, "+", 456]

    i, j = 0, -1
    while j < len(expr) - 1:
        j += 1
        if expr[j] not in operations:
            continue
        deq.append(int("".join(expr[i:j])))
        deq.append(expr[j])
        i = j + 1
    deq.append(int("".join(expr[i:j])))

    while len(deq) > 1:
        a = deq.popleft()
        op = deq.popleft()
        b = deq.popleft()
        if op == "+":
            deq.appendleft(a + b)
        elif op == "-":
            deq.appendleft(a - b)
        elif op == "x":
            deq.appendleft(a * b)
        elif op == "/":
            deq.appendleft(int(a / b))

    result = str(deq[0])
    for num, word in dic.items():
        result = result.replace(num, word)

    return (expr, result)


print(*solution(input().rstrip("\n")), sep="\n")
