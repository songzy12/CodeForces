n = int(input())
a = list(map(int, input().split()))

import math


def solve(a):
    res = a[0]
    for i in range(1, len(a)):
        res = math.gcd(res, a[i])

    from collections import defaultdict
    m = defaultdict(int)
    d = 2
    while res != 1:
        while res % d == 0:
            res = res / d
            m[d] += 1
        d += 1

    res = 1
    for k in m:
        res *= m[k] + 1
    return res


print(solve(a))
