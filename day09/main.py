from collections import Counter
import numpy as np
from scipy.ndimage import minimum_filter, label

x = np.genfromtxt("input.txt", delimiter=1, dtype=np.uint8)
filtered = minimum_filter(x, footprint=[[0,1,0],[1,1,1],[0,1,0]])
mask = (x == filtered) & (x < 9)
print(sum(np.where(mask, x+1, 0).flatten()))

areas = label(x < 9)[0]
largest = Counter(areas.flatten()).most_common(4)[1:]
print(np.prod([v for _, v in largest]))
