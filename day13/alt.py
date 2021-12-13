with open("input.txt") as f:
    grps = [x.strip().split() for x in f.read().split("\n\n")]

ns = set((int(x), int(y)) for x, y in [l.split(",") for l in grps[0]])
fs = [[k, int(v)] for k, v in [l.split("=") for l in grps[1][2::3]]]

for i, (k, v) in enumerate(fs):
    if k == "x":
        ns = set((x, y) if x < v else (2*v - x, y) for x, y in ns)
    else:
        ns = set((x, y) if y < v else (x, 2*v - y) for x, y in ns)
    if i == 0:
        print(len(ns))

max_x, max_y = [max(v) for v in zip(*ns)]
for y in range(max_y+1):
    for x in range(max_x+1):
        if (x,y) in ns:
            print(end="#")
        else:
            print(end=" ")
    print()
