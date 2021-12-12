from collections import Counter, defaultdict, deque

d = defaultdict(list)
with open("input.txt") as f:
    for u, v in [x.strip().split("-") for x in f]:
        d[u].append(v)
        d[v].append(u)

def condition_part2(v, p):
    if v in ("start", "end"): 
        return False
    for k, v in Counter(p).items():
        if k == k.lower() and v > 1: 
            return False
    return True

for is_part2 in [False, True]:
    count = 0
    path = ["start"]
    q = deque()
    q.append(path.copy())

    while q:
        curr_path = q.popleft()
        last = curr_path[-1]

        if last == "end":
            count += 1

        for v in d[last]:
            if v != v.lower() or v not in curr_path or (is_part2 and condition_part2(v, curr_path)):
                p = curr_path.copy()
                p.append(v)
                q.append(p)
    print(count)