from itertools import product

def is_valid(dx, dy, target):
    tminx, tmaxx, tminy, tmaxy = target
    pos_x, pos_y = 0, 0
    while pos_x <= tmaxx and pos_y >= tminy:
        pos_x, pos_y, dx, dy = pos_x+dx, pos_y+dy, max(0, dx-1), dy-1
        if tminx <= pos_x <= tmaxx and tminy <= pos_y <= tmaxy:
            return True
    return False

gauss = lambda x: (x+1) * x // 2

target = 150, 171, -129, -70
velocities = [dy for dx, dy in product(range(1000), range(-1000, 1000)) if is_valid(dx, dy, target)]
print(gauss(max(velocities)))
print(len(velocities))
