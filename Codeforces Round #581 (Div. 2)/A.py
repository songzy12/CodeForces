s = int(input(), 2)


def solve(s):
    if s == 0:
        return 0
    import math
    t = int(math.log(s, 4))

    # print(s, math.log(s, 4), t, 4**t)

    if 4**t >= s: 
        t -= 1
    return t + 1


print(solve(s))
# NOTE: 4 ** int(math.log(s, 4)) may > s, e.g.
# when s = 1267650600228229401496703205375