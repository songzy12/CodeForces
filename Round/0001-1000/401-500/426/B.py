n, k = map(int, raw_input().split())
s = raw_input()

# the first sweep, find the first and last index of each char
# the second sweep, record the number of active chars currently

def valid_(a, b, k):
    c = 0
    for i in range(26):
        if a[i] and b[i]:
            c += 1
    return c <= k

def valid(s, k):
    a = [0 for i in range(26)]
    b = [0 for i in range(26)]
    for c in s:
        b[ord(c) - ord('A')] += 1
    for i in range(len(s)):
        a[ord(s[i])-ord('A')] += 1
        if i > 0:
            b[ord(s[i-1])-ord('A')] -= 1
        if not valid_(a, b, k):
            return False
    return True
        

##def valid(s, k):
##    pre = []
##    cur = set()
##    for i in range(len(s)):
##        cur.add(s[i])
##        pre = pre + [set(cur)]
##    suf = []
##    cur = set()
##    for i in range(len(s)-1,-1,-1):
##        cur.add(s[i])
##        suf = [set(cur)] + suf
##
##    for i in range(len(s)):
##        temp = pre[i].intersection(suf[i])
##        if len(temp) > k:
##            return False
##    return True

if valid(s, k):
    print 'NO'
else:
    print 'YES'
    
