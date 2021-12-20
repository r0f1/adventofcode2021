import numpy as np
from scipy.ndimage import generic_filter

with open("input.txt") as f:
    l, img = f.read().split("\n\n")

l = [int(c == '#') for c in l]
img = np.pad(np.array([[int(c == '#') for c in r] for r in img.strip().split("\n")], dtype="int"), (51,51))

for k in range(50):
    img = generic_filter(img, lambda a: l[sum(d*2**i for i, d in enumerate(a.astype(int)[::-1]))], size=3)
    if k+1 in (2,50):
        print(np.count_nonzero(img))
