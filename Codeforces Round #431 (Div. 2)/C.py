def compute_n(k):
    n = (2*k+0.25)**0.5 + 0.5
    return int(n)

k = int(raw_input())
ans = []
import string
cur = iter(string.lowercase)
while k:
    n = compute_n(k)
    k -= n*(n-1)/2
    ans += [cur.next() * n]
if not ans:
    print 'a'
else:
    print ''.join(ans)
