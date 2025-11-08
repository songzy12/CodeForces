# https://codeforces.com/blog/entry/54590
from sys import stdout
n = int(raw_input())

found = False

print '?', '0' * n


stdout.flush()
a = int(raw_input())

print '?', '0' * (n-1) + '1'


stdout.flush()
b = int(raw_input())

def compute(length, num0, num1):
    return (length+num1-num0)/2, (length-num1+num0)/2

cnt = compute(1, a, b)

def binary_search(l, r, target):
    # [l ,r] contain target
    while l < r:
        m = (l + r) / 2
        print '?', '0' * (l - 1) + '1' * (m - l + 1) + '0' * (n - m)

        stdout.flush()
        b = int(raw_input())
        cnt = compute(m - l + 1, a, b)
        # print l, m, r, cnt
        if cnt[target]:
            r = m
        else:
            l = m + 1
    return l
    

if cnt[0]:
    # find pos of 1
    r = binary_search(1, n - 1, 1)
    print '!', n, r
else:
    # find pos of 0
    l = binary_search(1, n - 1, 0)
    print '!', l, n

stdout.flush()
