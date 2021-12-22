from itertools import product

with open("input.txt") as f:
    lines = [x.strip() for x in f]

lights = set()

for linenr, line in enumerate(lines):
    cmd, regionstr = line.split()
    xstr, ystr, zstr = regionstr.split(",")
    xstart, xend = [int(n) for n in xstr[2:].split("..")]
    ystart, yend = [int(n) for n in ystr[2:].split("..")]
    zstart, zend = [int(n) for n in zstr[2:].split("..")]
    
    if xstart < -50: break

    for c in product(range(xstart, xend+1), range(ystart, yend+1), range(zstart, zend+1)):
        if cmd == "on":
            lights.add(c)
        else:
            lights.discard(c)

print(len(lights))
