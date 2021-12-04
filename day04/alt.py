# From 4HbQ on Reddit
import numpy as np

n, *b = open("input.txt")
b = np.loadtxt(b, int).reshape(-1,5,5)

for n in map(int, n.split(',')):
    b[b == n] = -1
    m = (b == -1)
    win = (m.all(1) | m.all(2)).any(1)
    if win.any():
        print((b * ~m)[win].sum() * n)
        b = b[~win]
