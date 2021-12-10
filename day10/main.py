from functools import reduce
from statistics import median

with open("input.txt") as f:
    lines = [x.strip() for x in f]

bs = {"(": ")", "[": "]", "{": "}", "<": ">"}
d1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
d2 = {"(": 1, "[": 2, "{": 3, "<": 4}

part1 = []
part2 = []
for line in lines:
    stack = []
    for c in line:
        if c in "<{[(": 
            stack.append(c)
        else:
            if bs[stack.pop()] != c:
                part1.append(d1[c])
                break
    else:
        part2.append(reduce(lambda x, y: x*5 + d2[y], stack[::-1], 0))

print(sum(part1))
print(median(part2))
