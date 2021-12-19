from itertools import combinations
from more_itertools import flatten

def permute(coords):
    x, y, z = coords
    return [(x, y, z), (y, z, x), (z, x, y), (z, y, -x), (y, x, -z), (x, z, -y),
            (x, -y, -z), (y, -z, -x), (z, -x, -y), (z, -y, x), (y, -x, z), (x, -z, y),
            (-x, y, -z), (-y, z, -x), (-z, x, -y), (-z, y, x), (-y, x, z), (-x, z, y),
            (-x, -y, z), (-y, -z, x), (-z, -x, y), (-z, -y, -x), (-y, -x, -z), (-x, -z, -y)]

def all_possible_orientations(beacon):
    return zip(*(permute(c) for c in beacon))

tuple_sum = lambda t1, t2: tuple(a + b  for a, b in zip(t1, t2))
tuple_dif = lambda t1, t2: tuple(a - b  for a, b in zip(t1, t2))
cityblock = lambda t1, t2: sum(abs(a-b) for a, b in zip(t1, t2))

def commons(coords_a, coords_b, delta):
    s = set()
    for i in coords_a:
        s.add(i)
    for j in coords_b:
        s.add(tuple_sum(j, delta))
    return len(coords_a) + len(coords_b) - len(s)

def match(coords_a, beacon_b):
    for coords_b in all_possible_orientations(beacon_b):
        for i, ca in enumerate(coords_a):
            for cb in coords_b[i:]:
                delta = tuple_dif(ca, cb)
                if commons(coords_a, coords_b, delta) >= 12:
                    return [tuple_sum(c, delta) for c in coords_b], delta 

def full_match(scanners):
    detted = [scanners.pop()]
    diffs = []

    while scanners:
        print(len(scanners))
        for i, s2 in enumerate(scanners):
            for s1 in detted:
                vals = match(s1, s2)
                if vals is not None:
                    mch, diff = vals
                    detted.append(mch)
                    diffs.append(diff)
                    scanners.pop(i)
                    break
            else:
                continue
            break
    return detted, diffs

with open("input.txt") as f:
    scanners = [[tuple(int(n) for n in s.split(",")) for s in x.strip().split("\n")[1:]] for x in f.read().split("\n\n")]

beacons, diffs = full_match(scanners)
print(len(set(flatten(beacons))))
print(max(cityblock(*p) for p in combinations([(0,0,0)] + diffs, 2)))
