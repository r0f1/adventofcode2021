import numpy as np
from skimage.draw import line

with open("input.txt") as f:
    coords = [[[int(k) for k in c.split(",")] for c in x.strip().split(" -> ")] for x in f]

arr1 = np.zeros((1000,1000), dtype=np.uint8)
arr2 = np.zeros((1000,1000), dtype=np.uint8)

for ((x1, y1), (x2, y2)) in coords:
    rr, cc = line(x1, y1, x2, y2)
    if x1 == x2 or y1 == y2:
        arr1[rr, cc] += 1
    arr2[rr, cc] += 1

print(len(arr1[arr1 > 1]))
print(len(arr2[arr2 > 1]))
