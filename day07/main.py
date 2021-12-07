with open("input.txt") as f:
    pos = [int(x) for x in list(f)[0].strip().split(",")]

def f(n): return int(n*(n+1) / 2)

print(min([sum([  abs(p - i)  for p in pos]) for i in range(max(pos))]))
print(min([sum([f(abs(p - i)) for p in pos]) for i in range(max(pos))]))
