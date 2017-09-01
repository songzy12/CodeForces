n = int(raw_input())
y = map(int, raw_input().split())

def check_same(x0, y0, x1, y1, x2, y2):
    return (y1-y0)*(x2-x0) == (x1-x0)*(y2-y0)

def check(k):
    # y_0 is paired with y_k

    left = []
    
    for i in range(n):
        if i == 0 or i == k:
            continue
        if not check_same(0, y[0], k, y[k], i, y[i]):
            left.append(i)
    if not left:
        return False
    if len(left) == 1:
        return True
    if not (y[k]-y[0])*(left[1]-left[0]) == (y[left[1]]-y[left[0]])*(k-0):
        return False
    for i in range(2, len(left)):
        if not check_same(left[0], y[left[0]], left[1], y[left[1]], left[i], y[left[i]]):
            return False
    return True

def valid():
    for k in range(2, n):
        if check(k):
            return True
    for i in range(3, n):
        if not check_same(1, y[1], 2, y[2], i, y[i]):
            return False
    return not check_same(0, y[0], 1, y[1], 2, y[2])

print 'Yes' if valid() else 'No'
