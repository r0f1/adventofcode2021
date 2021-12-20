import numpy as np
from scipy.ndimage import generic_filter

with open("input.txt") as f:
    l, img = f.read().split("\n\n")

l = [0 if c == '.' else 1 for c in l]
img = np.array([[0 if c == '.' else 1 for c in row] for row in img.strip().split("\n")], dtype="int")

img = np.pad(img, (50,50))
for k in range(50):
    img = generic_filter(img, lambda a: l[sum(d*2**i for i, d in enumerate(a.astype(int)[::-1]))], size=3)
    if k in (1,49):
        print(np.count_nonzero(img))
