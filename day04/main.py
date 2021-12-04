from more_itertools import chunked
import numpy as np

with open("input.txt") as f:
    lines = [x.strip() for x in f]

ns = [int(x) for x in lines[0].split(",")]
boards = [np.array([[int(x) for x in c.split()] for c in b[1:]]) for b in chunked(lines[1:], 6)]

def is_winner(board, numbers):
    for row in board:
        if all(n in numbers for n in row):
            return True
    for col in board.T:
        if all(n in numbers for n in col):
            return True
    return False

winner_idxs = []
number_idxs = []

for idx in range(5, len(ns)+1):
    for b_idx, b in enumerate(boards):
        if b_idx not in winner_idxs and is_winner(b, set(ns[:idx])):
            winner_idxs.append(b_idx)
            number_idxs.append(idx)
    if len(winner_idxs) == len(boards):
        break

print(sum([n for n in boards[winner_idxs[0]].flatten()  if n not in ns[:number_idxs[0]]])  * ns[number_idxs[0]-1])
print(sum([n for n in boards[winner_idxs[-1]].flatten() if n not in ns[:number_idxs[-1]]]) * ns[number_idxs[-1]-1])
