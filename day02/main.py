
with open("input.txt") as f:
    cmds = [(c[0], int(c[1])) for c in [x.split() for x in f]]

x, d = 0, 0
for c, i in cmds:
    if c == "down": d += i
    elif c == "up": d -= i
    else: x += i

print(x*d)

x, d, a = 0, 0, 0
for c, i in cmds:
    if c == "down": a += i
    elif c == "up": a -= i
    else: x += i; d += a*i

print(x*d)
