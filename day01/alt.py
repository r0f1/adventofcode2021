with open("input.txt") as f:
    ns = [int(x) for x in f]

print(sum(x < y for x, y in zip(ns, ns[1:])))
print(sum(x < y for x, y in zip(ns, ns[3:])))
