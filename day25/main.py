from scipy.ndimage import generic_filter
import numpy as np

d = {".": 0, ">": 1, "v": 2}
with open("input.txt") as f:
    lines = [[d[c] for c in list(x.strip())] for x in f]

arr = np.array(lines)

def move_east(a):
    if a[4] == 0 and a[3] == 1: return 1
    if a[4] == 1 and a[5] == 0: return 0
    return a[4]

def move_south(a):
    if a[4] == 0 and a[1] == 2: return 2
    if a[4] == 2 and a[7] == 0: return 0
    return a[4]

i = 1
while True:
    prev = arr
    arr = generic_filter(arr, move_east,  size=3, mode="wrap")
    arr = generic_filter(arr, move_south, size=3, mode="wrap")
    if np.array_equal(prev, arr):
        print(i)
        break
    i += 1
