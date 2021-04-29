good = {k: True for k in raw_input()}
p = raw_input()
index = p.find('*')
n = int(raw_input())
for i in range(n):
    s = raw_input()
    def check(s):        

        def check_good(p, q):
            if len(p) != len(q):
                return False
            for i in range(len(p)):
                if p[i] != '?':
                    if p[i] != q[i]:
                        return False
                else:
                    if q[i] not in good:
                        return False
            return True

        def check_bad(t):
            for c in t:
                if c in good:
                    return False
            return True

        
        if index == -1:
            return check_good(p, s)
        rindex = len(p) - index - 1
        if rindex == 0:
            return check_good(p[:index], s[:index]) and \
                   check_bad(s[index:])
        if len(s) < index + rindex: # len matters
            return False
        return check_good(p[:index], s[:index]) and \
               check_good(p[-rindex:], s[-rindex:]) and \
               check_bad(s[index:-rindex]) # offset
    print "YES" if check(s) else "NO"
