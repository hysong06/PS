import functools
import sys

input = sys.stdin.readline

"""
src = "abkdeghilmn@oprstuwy"
order = {char: i for i, char in enumerate(src)}
"""
order = {
    "a": 0,
    "b": 1,
    "k": 2,
    "d": 3,
    "e": 4,
    "g": 5,
    "h": 6,
    "i": 7,
    "l": 8,
    "m": 9,
    "n": 10,
    "@": 11,
    "o": 12,
    "p": 13,
    "r": 14,
    "s": 15,
    "t": 16,
    "u": 17,
    "w": 18,
    "y": 19,
}


def compare(s1, s2):
    for ch1, ch2 in zip(s1, s2):
        if order[ch1] < order[ch2]:
            return -1
        if order[ch1] > order[ch2]:
            return 1
    return -1 if len(s1) < len(s2) else 1


N = int(input())
words = [input().rstrip().replace("ng", "@") for _ in range(N)]
words.sort(key=functools.cmp_to_key(compare))
for word in words:
    print(word.replace("@", "ng"))
