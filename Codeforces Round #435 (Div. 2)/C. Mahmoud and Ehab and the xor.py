# input x, n
# x, n in range [0, 10**5]
# find a set of n elements whose xor sum is x

n, x = map(int, raw_input().split())

if n == 1:
    print 'YES'
    print x    
elif n == 2:
    if x == 0:
        print 'NO'
    else:
        print 'YES'
        print 0, x
# handle n == 1 and n == 2
else:
    print 'YES'
    
    s = 0
    for i in range(1, n-2):
        print i,
        s ^= i
    # there are 3 numbers left

    pw = (10**5) << 1
    if s ^ x != 0:
        print pw, pw ^ x ^ s, 0
    else:
        print pw, pw << 1, pw ^ (pw << 1) ^ x ^ s 
