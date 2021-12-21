from itertools import cycle
from functools import lru_cache

# Part 1
players = [8, 2]
scores = [0, 0]

def create_dye():
    for n in cycle(range(1,101)):
        yield n

dye = create_dye()
ptr = 0
rolls = 0
while all(s < 1000 for s in scores):
    players[ptr] = (players[ptr] + sum(next(dye) for _ in range(3)) - 1) % 10 + 1
    scores[ptr] += players[ptr]
    rolls += 3
    ptr = (ptr + 1) % 2

print(min(scores) * rolls)

# Part 2
@lru_cache(maxsize=None)
def search(p1, s1, p2, s2):
    w1, w2 = 0, 0
    p1_initial = p1
    s1_initial = s1
    for s in [i+j+k for i in (1,2,3) for j in (1,2,3) for k in (1,2,3)]:
        p1 = (p1_initial + s - 1) % 10 + 1
        s1 = s1_initial + p1
        if s1 >= 21:
            w1 += 1
        else:
            r2, r1 = search(p2, s2, p1, s1)
            w1, w2 = w1+r1, w2+r2
    return w1, w2

print(max(search(8, 0, 2, 0)))
