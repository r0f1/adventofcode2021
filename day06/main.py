from collections import Counter, defaultdict

with open("input.txt") as f:
    c = Counter([int(x) for x in list(f)[0].split(",")])

for i in range(80): # replace by 256 for part 2
    d = defaultdict(int)
    for k, v in sorted(c.items()):
        if k == 0:
            d[6] += v
            d[8] = v
        else:
            d[k-1] += v
    c = d

print(sum(c.values()))
