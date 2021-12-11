import numpy as np
from scipy.ndimage import generic_filter

x = np.genfromtxt("input.txt", delimiter=1, dtype=int)

def func(arr):
    a = arr.tolist()
    if a[4] >= 0:
        return a[4] + sum(x > 9 for x in a[:4]+a[5:])
    return a[4]

count = 0
for i in range(10000):
    if i == 100:
        print(count)
    if np.count_nonzero(x == 0) == 100:
        print(i)
        break
    x += 1
    while True:
        k = (x > 9)
        f = generic_filter(x, func, size=3, mode="constant")
        f[k] = -1
        if (x == f).all():
            count += np.count_nonzero(x < 0)
            x[x == -1] = 0
            break
        x = f
