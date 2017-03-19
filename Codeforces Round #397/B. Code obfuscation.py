import string
lower = string.lowercase[:26]

s = raw_input()
def check(s):
    if s and s[0] != 'a':
        return False
    cur = 'a'
    for c in s:
        if ord(c) - ord(cur) <= 0:
            continue
        if ord(c) - ord(cur) == 1:
            cur = c
            continue
        return False
    return True
print 'YES' if check(s) else 'NO'
    
