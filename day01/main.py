from more_itertools import pairwise, windowed

with open("input.txt") as f:
    depths = [int(x) for x in f]

print(sum(b > a for a, b in pairwise(depths)))
print(sum(sum(b) > sum(a) for a, b in pairwise(windowed(depths, 3))))
