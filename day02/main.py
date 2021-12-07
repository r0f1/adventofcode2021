with open("input.txt") as f:
    cmds = [(c[0], int(c[1])) for c in [x.split() for x in f]]

x, d1, d2, a = 0, 0, 0, 0
for c, i in cmds:
    if c == "down": d1 += i; a += i
    elif c == "up": d1 -= i; a -= i
    else: x += i; d2 += a*i

print(x*d1, x*d2)
