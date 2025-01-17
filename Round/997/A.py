# https://codeforces.com/contest/2056/problem/0

T = int(input())

for t in range(T):
    n, m = map(int, input().split())
    x, y = map(int, input().split())
    res = 2*m
    for _ in range(n-1):
        x, y = map(int, input().split())
        res += x + y
    print(2*res)
