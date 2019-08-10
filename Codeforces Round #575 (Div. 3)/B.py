# https://codeforces.com/blog/entry/68655

q = int(input())

import sys
# NOTE: TLE for slow read in
cin = lambda: map(int, sys.stdin.readline().split()) 

for _ in range(q):
    n, k = cin()
    a = list(cin())

    def solve(a):
        res = []
        cnt = 0
        for i, t in enumerate(a):
            if t % 2 == 1:
                cnt += 1
                if cnt < k:
                    res.append(i + 1)
        if cnt < k or (cnt - k) % 2 == 1:
            return []
        res.append(n)
        return res  # why TLE?

    p = solve(a)
    if not p:
        print("NO")
    else:
        print("YES")
        print(*p)
