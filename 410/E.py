n = int(raw_input())
a = raw_input().split()
from collections import defaultdict
m = defaultdict(list)
for i, v in enumerate(a):
    m[int(v)].append(i+1)

p = [-1 for i in range(len(a)+1)]
cur = len(a)

while m[-1]:
    temp = m[-1][0]
    m[-1].pop(0)
    p[temp] = cur
    cur -= 1
    while temp in m:
        temp = m[temp][0]
        p[temp] = cur
        cur -= 1

print ' '.join(map(str, p[1:]))
    
// topologically sort