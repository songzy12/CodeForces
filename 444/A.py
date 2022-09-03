s = raw_input()

def check():
    i = len(s) - 1
    cnt = 0
    while i >= 0:
        if s[i] == '0':
            cnt += 1
        else:
            if cnt >= 6:
                return True
        i -= 1
    return False

print 'yes' if check() else 'no'

# need to be positive 
