from collections import Counter, defaultdict, deque

d = defaultdict(list)
with open("input.txt") as f:
    for u, v in [x.strip().split("-") for x in f]:
        d[u].append(v)
        d[v].append(u)

def condition_part2(v, p):
    return v not in ("start", "end") and all(v <= 1 for k, v in Counter(p).items() if k.islower())

for is_part2 in [False, True]:
    count = 0
    q = deque([["start"]])

    while q:
        path = q.popleft()
        last = path[-1]

        if last == "end":
            count += 1
            continue

        for v in d[last]:
            if v.isupper() or v not in path or (is_part2 and condition_part2(v, path)):
                p = path.copy()
                p.append(v)
                q.append(p)
    print(count)