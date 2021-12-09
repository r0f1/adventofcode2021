from collections import Counter
import numpy as np
from scipy.ndimage import generic_filter, label

x = np.genfromtxt("input.txt", delimiter=1, dtype=np.uint8)
mask = generic_filter(x, lambda x: x[2] < min(x[:2]) and x[2] < min(x[3:]), footprint=[[0,1,0],[1,1,1],[0,1,0]], mode="constant", cval=9)
print(np.count_nonzero(mask) + int((x*mask).sum().sum()))

areas, _ = label((x < 9).astype(int))
unique, counts = np.unique(areas, return_counts=True)
c = Counter(areas.flatten())
print(np.prod([v for _, v in c.most_common(4)[1:]]))
