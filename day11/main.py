import numpy as np
from scipy.ndimage import generic_filter

x = np.genfromtxt("input.txt", delimiter=1, dtype=int)

def func(arr):
    a = arr.tolist()
    if a[4] >= 0:
        return min(10, a[4] + sum(x == 10 for x in a[:4]+a[5:]))
    return a[4]

def calc_energies(x):
    while True:
        k = (x == 10)
        f = generic_filter(x, func, size=3, mode="constant")
        f[k] = -1
        if (x == f).all():
            x[x == -1] = 10
            return x
        x = f

count = 0
for i in range(10000):
    if i == 100:
        print(count)
    if np.count_nonzero(x == 0) == 100:
        print(i)
        break
    x = np.clip(x+1, 0, 10)
    x = calc_energies(x)
    count += np.count_nonzero(x == 10)
    x[x == 10] = 0
