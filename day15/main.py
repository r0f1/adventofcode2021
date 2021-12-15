from networkx import grid_2d_graph, shortest_path_length, DiGraph
import numpy as np
from itertools import product

def solve(weights):
    n = len(weights)
    G = grid_2d_graph(n, n, create_using=DiGraph)
    for u, v in G.edges:
        G[u][v]["weight"] = weights[v[1]][v[0]]
    print(shortest_path_length(G, (0,0), (n-1,n-1), "weight"))

with open("input.txt") as f:
    risk = [[int(i) for i in list(x.strip())] for x in f]

solve(risk)

n = len(risk)
arr = np.zeros((n*5, n*5), dtype=np.uint8)
for row, col in product(range(n*5), range(n*5)):
    arr[col][row] = (risk[col % n][row % n] - 1 + (row//n) + (col//n)) % 9 + 1

solve(arr)
