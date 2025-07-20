##from sympy.ntheory import factorint

n = int(raw_input())

def valid(m, n):
    if (m + n) % 3 != 0:
        return False
    t = (m + n) / 3
    if m - t < 0:
        return False
    if n - t < 0:
        return False
    return True

## not only as a part, but also as a whole

def check(a, b):
    temp = int(round((a*b)**(1.0/3)))
    if temp * temp * temp != a * b:
        return False
    return a % temp == 0 and b % temp == 0

##def check(a, b):
##    pa = factorint(a)
##    pb = factorint(b)
##    if set(pa.keys()) != set(pb.keys()):
##        return False
##    for base, exp in pa.items():
##        if base not in pb:
##            return False
##        if not valid(exp, pb[base]):
##            return False
##    return True

##def check(a, b):
##    cur = 2
##    while a != 1 and b != 1 and cur <= a and cur <= b:
##        #print a, b
##        if a % cur == 0 and b % cur == 0:
##            m = 0
##            n = 0
##            while a % cur == 0:
##                a /= cur
##                m += 1
##            while b % cur == 0:
##                b /= cur
##                n += 1
##            if not valid(m, n):
##                return False
##        if a % cur == 0 or b % cur == 0:
##            return False
##        cur += 1
##    if a != 1 or b != 1:
##        return False
##    return True
                

for i in range(n):
    a, b = map(int, raw_input().split())
    print 'Yes' if check(a, b) else 'No'
