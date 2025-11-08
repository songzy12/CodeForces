n = int(raw_input())

a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

n -= 1

if not n:
    print 0
else:
    print min(a, b) + (n - 1) * min([a, b, c])
