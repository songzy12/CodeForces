l, r, x, y, k = map(int, raw_input().split())

def valid():
    for b in range(max(x, l / k), min(y, r / k) + 1):
        if l <= b * k <= r:
            return True
    return False

##def valid():
##    # hack: 4 4 1 2 3
##    # even when the [min, max] cover [x, y], it may not overlap with [x, y]
##    # since [min, max] may just [min, min+k, min+2k] and skip [x, y]
##    return not (y < l * 1.0 / k or x > r * 1.0 / k) 


print 'YES' if valid() else 'NO'
