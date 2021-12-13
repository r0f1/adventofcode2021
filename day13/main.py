import numpy as np
np.set_printoptions(linewidth=1000)

with open("input.txt") as f:
    grps = [x.strip().split() for x in f.read().split("\n\n")]

ns = [[int(x), int(y)] for x, y in [l.split(",") for l in grps[0]]]
fs = [[k, int(v)] for k, v in [l.split("=") for l in grps[1][2::3]]]

arr = np.zeros((10000, 10000), dtype=np.uint8)
for x, y in ns:
    arr[y, x] = 1

for i, (k, v) in enumerate(fs):
    if k == "x":
        a1 = arr[:,:v]
        a2 = arr[:,2*v:v:-1]
    else:
        a1 = arr[:v,:]
        a2 = arr[2*v:v:-1,:]
    arr = np.clip(a1 + a2, 0, 1)
    if i == 0:
        print(np.count_nonzero(arr))

print(np.array2string(arr, separator='', formatter={"int":{0:' ',1:'█'}.get}))
