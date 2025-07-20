# https://codeforces.com/contest/891/problem/B

# 1: no one can be in their original position
n = int(raw_input())
b = map(int, raw_input().split())

c = [(t, i) for i, t in enumerate(b)]
c.sort()

d = [0 for i in range(n)]

for i in range(n - 1):
    d[c[i+1][-1]] = c[i][0]
d[c[0][-1]] = c[-1][0]

for t in d:
    print t,

# It doesn't mean sort and then shift, even though that what it says.
# It means: for a sorted array we can just cyclic shift.
# For an un-sorted array, we do the same thing:
# replace the i-th smallest element with the (i + 1)-th smallest,
# and replace the largest with the smallest.
