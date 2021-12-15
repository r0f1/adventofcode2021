# From 4HbQ on Reddit
import numpy as np
from skimage.graph import MCP

G = np.genfromtxt("input.txt", delimiter=1)
H = np.block([[(G+i+j-1)%9+1 for i in range(5)] for j in range(5)])

f = lambda A: MCP(A, fully_connected=0).find_costs([(0,0)])[0][(-1,-1)] - A[0,0]
print(f(G), f(H))
