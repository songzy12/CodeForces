s = raw_input()

def compute(s):
    i = 0
    j = len(s) - 1
    ans = 0
    while i < j:
        if s[i] != s[j]:
            ans += 1
        i += 1
        j -= 1
    return ans

def is_valid(s):
    num = compute(s)
    if len(s) % 2 == 0:
        return num == 1
    return num == 1 or num == 0

print "YES" if is_valid(s) else "NO"
