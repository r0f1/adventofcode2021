from collections import Counter, defaultdict
from more_itertools import flatten

with open("input.txt") as f:
    lines1, lines2 = zip(*[x.strip().split(" | ") for x in f])

inputs, outputs = [x.split() for x in lines1], [x.split() for x in lines2]
c = Counter([len(x) for x in flatten(outputs)])
print(c[2]+c[3]+c[4]+c[7])

def identify(di):
    # 2 segments = 1
    # 3 segments = 7
    # 4 segments = 4
    # 5 segments = 2, 3, 5
    # 6 segments = 0, 6, 9
    # 7 segments = 8

    # 1 + 6 (and not 0, 9) = 8 -> 6 identified, c segment identified
    # 1 - c segment -> f segment identified
    # 3 (and not 2, 5) contains both c and f -> 3 identified
    # 5 does not have c or f -> 5 identified, e segment identified
    # 2 is the last 5 segment number -> 2 identified
    # 9 (and not 0) does not have e -> 9 identified -> 0 identified

    s = {1: set(di[2][0]), 4: set(di[4][0]), 7: set(di[3][0]), 8: set(di[7][0])}
    m = {}

    # identify 6 under the 6 segment digits
    one = list(s[1])
    for x in di[6]:
        if not all(o in x for o in one):
            s[6] = set(x)
            di[6].remove(x)
            if one[0] in s[6]: 
                m["f"], m["c"] = one
            else:
                m["c"], m["f"] = one
            break

    # identify 3 under 5 segment digits
    for x in di[5]:
        if m["f"] in x and m["c"] in x:
            s[3] = set(x)
            di[5].remove(x)
            break

    # identify 5 and 2 under the 5 segment digits
    x, y = di[5]
    if m["c"] not in x:
        s[5], s[2] = set(x), set(y)
    else:
        s[2], s[5] = set(x), set(y)

    m["e"] = (s[6] - s[5]).pop()

    # identify 9 and 0 under the 6 segment digits
    x, y = di[6]
    if m["e"] not in x:
        s[9], s[0] = set(x), set(y)
    else:
        s[0], s[9] = set(x), set(y)
    return s

def decode(x, s):
    for k, v in s.items():
        if len(x) == len(v) and all(c in v for c in x): 
            return k

res = []
for i, o in zip(inputs, outputs):
    di = defaultdict(list)
    for x in i:
        di[len(x)].append(x)
    s = identify(di)
    res.append(int("".join(str(a) for a in [decode(x, s) for x in o])))

print(sum(res))
