# https://codeforces.com/contest/2051/problem/A
#
# If a_i > b_{i+1}, then participate.

def compute(a, b, n):
    res = a[-1]
    for i in range(n-1):
        if a[i] > b[i+1]:
            res += a[i] - b[i+1]
    return res

T = int(input())
for t in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(compute(a, b, n))