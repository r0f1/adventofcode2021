# From michalopler on Reddit
L = open('input.txt').read()
S = [L.count(str(i)) for i in range(9)]

for i in range(257):
    if i in (80,256):
        print(sum(S))
    S[(i+7) % 9] += S[i % 9]
