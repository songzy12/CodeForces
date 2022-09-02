def all_equal(l):
    pivot = l[0]
    for _, e in enumerate(l):
        if e != pivot:
            return False
    return True


def check(i, a, b, n):
    if a[i] == b[i]:
        return True
    if a[i] > b[i]:
        return False
    if b[(i + 1) % n] < b[i] - 1:
        return False
        
    if (i + 1) % n == 0:
        return True
    return check((i + 1) % n, a, b, n)


T = int(input())
for t in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if all_equal(b):
        print('Yes')
        continue
    # for each position i, if ai != bi, then we need ai to be increased to bi.
    # which means, we need to have aj in the right of ai that aj <= bj and bj >= bi - 1.
    print('Yes' if check(0, a, b, n) else 'No')
