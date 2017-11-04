c = [0] + map(int, raw_input().split())

def same(n1, n2, n3, n4):
    return c[n1] == c[n2] == c[n3] == c[n4]

def check():
    if c[5] == c[6] == c[7] == c[8] and \
       c[21] == c[22] == c[23] == c[24]:
        if c[9] == c[10] == c[20] == c[18] and \
           c[19] == c[17] == c[1] == c[2] and \
           c[3] == c[4] == c[13] == c[15] and \
           c[14] == c[16] == c[11] == c[12]:
            return True
        if c[9] == c[10] == c[13] == c[15] and \
           c[14] == c[16] == c[1] == c[2] and \
           c[3] == c[4] == c[18] == c[20] and \
           c[17] == c[19] == c[11] == c[12]:
            return True
    if same(13, 14, 15, 16) and same(17, 18, 19, 20):
        if same(5,7,2,4) and same(1,3,21,23) and \
           same(22,24,10,12) and same(9,11,6,8):
            return True
        if same(5,7,10,12) and same(9,11,21,23) and \
           same(22,24,2,4) and same(1,3,6,8):
            return True
    if same(1,2,3,4) and same(9,10,11,12):
        if same(7,8,17,18) and same(19,20,21,22) and \
           same(23,24,13,14) and same(15,16,5,6):
            return True
        if same(7,8,13,14) and same(19,20,5,6) and \
           same(23,24,17,18) and same(15,16,21,22):
            return True
    return False

print 'YES' if check() else 'NO'
        
