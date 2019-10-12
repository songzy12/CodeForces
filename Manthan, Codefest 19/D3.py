# https://codeforces.com/contest/1208/problem/D

from sys import stdin, stdout
input = stdin.readline
print = stdout.write

# si is the sum of elements before the i-th element that are smaller than the i-th element.

# For every i from N to 1, let's say the value of the si is x. 
# So it means there are k smallest unused numbers whose sum is x.
# We simply put the k+1st number in the output permutation at this i, and continue to move left. 

# BIT and binary lifting
# https://codeforces.com/contest/1208/submission/59526098

import sys
input = sys.stdin.readline
 
nn = 18
bit=[0]*(2**nn+1)
 
def addbit(i, x):
    while i <= 2**nn:
        bit[i] += x
        i += i & (-i)
 
def getsum(i):
    ret = 0
    while i != 0:
        ret += bit[i]
        i -= i&(-i)
    return ret
 
def searchbit(x):
    l, sl = 0, 0
    d = 2**(nn-1)
    while d:
        m = l + d
        sm = sl + bit[m]
        if sm <= x:
            l, sl = m, sm
        d //= 2
    return l + 1
 
n = int(input())
l = list(map(int, input().split()))
for i in range(1, n + 1):
	addbit(i, i)
ans = [0 for _ in range(n)]
for i in range(n - 1, -1, -1):
	a = searchbit(l[i])
	addbit(a, -a)
	ans[i] = a
print(*ans)