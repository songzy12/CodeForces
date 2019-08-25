n, l, r = map(int, input().split())


def solve(n, l, r):
    min_ = (n-l) + 2**l-1
    max_ = (n-r) * 2**(r-1) + 2**r-1
    return min_, max_


min_, max_ = solve(n, l, r)
print(min_, max_)
