a, b, c, d = map(int, input().split())


def compute(x, y, d):
    if abs(x-y) >= d:
        return 0
    return d - abs(x-y)

a, b, c = sorted([a, b, c])
print(compute(a, b, d) + compute(b, c, d))
