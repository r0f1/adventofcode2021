from networkx import grid_2d_graph, shortest_path_length, DiGraph
import numpy as np
from itertools import product

def solve(weights):
    n = len(weights)
    G = grid_2d_graph(n, n, create_using=DiGraph)
    for u, v in G.edges:
        G[u][v]["weight"] = weights[v[1]][v[0]]
    print(shortest_path_length(G, (0,0), (n-1,n-1), "weight"))

risk = np.genfromtxt("input.txt", delimiter=1, dtype=int)
solve(risk)

n = len(risk)
arr = np.zeros((n*5, n*5), dtype=np.uint8)
for row, col in product(range(n*5), range(n*5)):
    arr[col][row] = risk[col % n][row % n] + (row//n) + (col//n)

arr[arr > 9] -= 9
solve(arr)
