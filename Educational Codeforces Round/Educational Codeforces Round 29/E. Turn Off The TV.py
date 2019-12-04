# https://codeforces.com/contest/863/problem/E

from sys import stdin, stdout
input = stdin.readline

n = int(input())
a = []
segments = []
for i in range(n):
    l, r = map(int, input().split())
    a.append([l, 1, i])
    a.append([r, -1, i])
    segments.append([l, r])

a.sort()
cur = 0

from collections import defaultdict
cnt = defaultdict(int)

t = 0
while t < len(a):
    side, delta, index = a[t]
    if delta == 1 and side - 1 not in cnt:  # NOTE: check this
        cnt[side - 1] = cur
    neg = 0
    while True:
        side, delta, index = a[t]
        if delta == 1:
            cur += 1
        else:
            neg += 1  # NOTE: check this
        if t + 1 < len(a) and a[t+1][0] == side:
            t += 1
        else:
            break
    cnt[side] = cur
    cur -= neg
    t += 1
    # print(side, delta, index, cur, cnt)

prefix = defaultdict(int)
cur = 0
for t in sorted(cnt.keys()):
    if cnt[t] == 1:
        cur += 1
    prefix[t] = cur

for i, segment in enumerate(segments):
    l, r = segment
    if prefix[r] - prefix[l - 1] == 0:
        print(i + 1)
        break
else:
    print(-1)
