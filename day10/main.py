from lark import Lark
from lark.exceptions import UnexpectedCharacters
from statistics import median

with open("input.txt") as f:
    lines = [x.strip() for x in f]

g = """
l: c +
c: (c1 | c2 | c3 | c4) *
c1: "(" c ")"
c2: "[" c "]"
c3: "{" c "}"
c4: "<" c ">"
"""

p = Lark(g, start="l")
part1 = []
remaining = []
for l in lines:
    try:
        p.parse(l)
    except UnexpectedCharacters as ex:
        part1.append(l[ex.pos_in_stream])
    except:
        remaining.append(l)

d = {")": 3, "]": 57, "}": 1197, ">": 25137}
print(sum(d[s] for s in part1))

def is_closing(a, b):
    return any([a == "(" and b == ")", a == "[" and b == "]", a == "{" and b == "}", a == "<" and b == ">"])

d = {"(": 1, "[": 2, "{": 3, "<": 4}
part2 = []
for line in remaining:
    stack = []
    for c in line:
        if len(stack) > 0 and is_closing(stack[-1], c):
            stack.pop()
        else:
            stack.append(c)
    score = 0
    for x in stack[::-1]:
        score *= 5
        score += d[x]
    part2.append(score)

print(median(part2))
