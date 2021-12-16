from math import prod

def convert_hex_to_bin(s):
    d = dict((f"{k:x}".upper(), f"{k:04b}") for k in range(16))
    return "".join(d[i] for i in s)

def parse_nr(s):
    ptr = 0
    res = []
    while True:
        res.append(s[ptr+1:ptr+5])
        if s[ptr] == "0":
            break
        ptr += 5
    return 5*len(res), int("".join(res), base=2)

def parse_msg(s):
    ptr = 0
    version = int(s[ptr:ptr+3],   base=2)
    type_id = int(s[ptr+3:ptr+6], base=2)
    ptr += 6
    if type_id == 4:
        p, n = parse_nr(s[ptr:])
        return version, n, ptr + p

    op = {
        0: sum, 1: prod, 2: min, 3: max, 
        5: lambda x: int(x[0] > x[1]),
        6: lambda x: int(x[0] < x[1]), 
        7: lambda x: int(x[0] == x[1])
    }

    res = version
    ns = []

    if s[ptr] == "0":
        len_subpackets = int(s[ptr+1:ptr+16], base=2)
        ptr += 16
        parse_until = ptr+len_subpackets

        while ptr < parse_until:
            v, n, p = parse_msg(s[ptr:])
            ptr += p
            res += v
            ns.append(n)
    else:
        n_subpackets = int(s[ptr+1:ptr+12], base=2)
        ptr += 12
        for _ in range(n_subpackets):
            v, n, p = parse_msg(s[ptr:])
            ptr += p
            res += v
            ns.append(n)
    
    return res, op[type_id](ns), ptr

with open("input.txt") as f:
    inp = f.read().strip()

part1, part2, _ = parse_msg(convert_hex_to_bin(inp))
print(part1)
print(part2)
