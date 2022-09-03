q = int(input())

import math

def convert(robot):
    x, y, f1, f2, f3, f4 = robot
    cur = [x, x, y, y]
    if f1:
        cur[0] = -math.inf
    if f2:
        cur[2] = math.inf        
    if f3:
        cur[1] = math.inf
    if f4:
        cur[3] = -math.inf
    return cur


def intersect(area0, area1):
    l0, r0, u0, d0 = area0
    l1, r1, u1, d1 = area1

    if l0 > r1 or l1 > r0:
        return None
    if u0 < d1 or u1 < d0:
        return None

    return max(l1, l0), min(r0, r1), min(u0, u1), max(d0, d1)

def extract(area):
    l, r, u, d = area
    x, y = None, None
    if l == -math.inf:
        x = r if r != math.inf else 0
    else:
        x = l if l != -math.inf else r

    if u == math.inf:
        y = d if d != -math.inf else 0
    else:
        y = u if u != math.inf else d
    return [x, y]


def solve(r):
    cur = [-math.inf, math.inf, math.inf, -math.inf]
    for robot in r:
        area = convert(robot)
        # print(robot, area)
        cur = intersect(cur, area)
        if cur == None:
            return 0, []
    return 1, extract(cur)


for _ in range(q):
    N = int(input())
    r = []
    for n in range(N):
        r.append(list(map(int, input().split())))
    p, q = solve(r)
    print(' '.join(map(str, [p] + q)))
