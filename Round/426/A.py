s, e = raw_input().split()
n = int(raw_input())
n %= 4
def compute(s, e, n):
    if n == 0 or n == 2:
        return 'undefined'
    sequence = 'v<^>'
    
    s = sequence.find(s)
    e = sequence.find(e)
    if n == 1:
        if e - s == 1 or e - s == -3:
            return 'cw'
        return 'ccw'
    if n == 3:
        if e - s == 1 or e - s == -3:
            return 'ccw'
        return 'cw'
print compute(s, e, n)
