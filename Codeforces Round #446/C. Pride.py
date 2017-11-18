n = int(raw_input())
a = map(int, raw_input().split())

def gcd(x, y):
    if x < y:
        x, y = y, x
    while x != y and y != 0:
        x, y = y, x % y
    return x

def one(a):
    b = []
    for i in range(1, len(a)):
        temp = gcd(a[i-1], a[i])
        if temp == 1:
            return True, []
        b.append(temp)
    return False, b

cnt = a.count(1) # there may be more than 1 in a
if cnt > 0:
    print n - cnt
else:
    t, b = one(a)
    while not t and len(b) > 1:
        cnt += 1
        a = b
        t, b = one(a)
    if not t:
        print -1
    else:
        print cnt + n        
        
