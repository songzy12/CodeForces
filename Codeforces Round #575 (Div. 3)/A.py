q = int(input())


def solve(a):
    a.sort()
    t1 = a[0] + a[2]
    t2 = a[1]
    if t1 <= t2:
        return t1
    return t1 + (t2 - t1) // 2


for _ in range(q):
    a = list(map(int, input().split()))
    print(solve(a))
