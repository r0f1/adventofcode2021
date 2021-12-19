# adapted from user 1vader on Reddit

from functools import reduce
from itertools import permutations
from math import ceil, floor

def add_left(x, n):
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    return [add_left(x[0], n), x[1]]


def add_right(x, n):
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    return [x[0], add_right(x[1], n)]


def split(x):
    if isinstance(x, int):
        if x > 9:
            return True, [floor(x / 2), ceil(x / 2)]
        return False, x
    a, b = x
    change, a = split(a)
    if change:
        return True, [a, b]
    change, b = split(b)
    return change, [a, b]

def explode(x, n=4):
    if isinstance(x, int):
        return False, None, x, None
    if n == 0:
        return True, x[0], 0, x[1]
    a, b = x
    exp, left, a, right = explode(a, n - 1)
    if exp:
        return True, left, [a, add_left(b, right)], None
    exp, left, b, right = explode(b, n - 1)
    if exp:
        return True, None, [add_right(a, left), b], right
    return False, None, x, None

def add(l, r):
    n = [l, r]
    while True:
        change, _, n, _ = explode(n)
        if change:
            continue
        change, n = split(n)
        if not change:
            break
    return n

def magnitude(n):
    if isinstance(n, int):
        return n
    return 3*magnitude(n[0]) + 2*magnitude(n[1])

with open("input.txt") as f:
    lines = [eval(x.strip()) for x in f]

print(magnitude(reduce(add, lines)))
print(max(magnitude(add(a, b)) for a, b in permutations(lines, 2)))
