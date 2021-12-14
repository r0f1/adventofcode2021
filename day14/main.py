from collections import Counter, defaultdict
from math import ceil

with open("input.txt") as f:
    lines = [x.strip() for x in f]

code = lines[0]
d = dict(l.split(" -> ") for l in lines[2:])
c = Counter("".join(t) for t in zip(code, code[1:]))

for _ in range(40): # replace with 10 for part 1
    k = defaultdict(int)
    for p, v in c.items():
        if p in d:
            i = d[p]
            k[p[0]+i] += v
            k[i+p[1]] += v
        else:
            k[p] = v
    c = k

k = defaultdict(int)
for p, v in c.items():
    k[p[0]] += v
    k[p[1]] += v

l = sorted(ceil(v/2) for _, v in k.items())
print(l[-1] - l[0])
