# Part 1
with open("input.txt") as f:
    cols = list(zip(*[[int(i) for i in x.strip()] for x in f]))

l = len(cols[0]) / 2
gamma = "".join("1" if sum(c) > l else "0" for c in cols)
epsilon = "".join("1" if x == "0" else "0" for x in gamma)
print(int(gamma, 2) * int(epsilon, 2))

# Part 2
with open("input.txt") as f:
    lines = [[int(i) for i in x.strip()] for x in f]

def life_support_rating(rows, n):
    ptr = 0
    while len(rows) > 1:
        k = n if sum(list(zip(*rows))[ptr]) >= len(rows) / 2 else (n+1) % 2
        rows = [r for r in rows if r[ptr] == k]
        ptr += 1
    return "".join(str(i) for i in rows[0])

oxygen = life_support_rating(lines, 1)
co2    = life_support_rating(lines, 0)
print(int(oxygen, 2) * int(co2, 2))
