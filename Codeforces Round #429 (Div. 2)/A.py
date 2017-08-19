n, k = map(int, raw_input().split())
s = raw_input()
from collections import Counter

def valid():
    c = Counter(s)
    for v in c.values():
        if v > k:
            return False
    return True

print "YES" if valid() else "NO"
