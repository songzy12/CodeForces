# https://codeforces.com/contest/2051/problem/B


def compute(n, a, b, c):
    day = n // (a + b + c)
    total = day * (a + b + c)
    if total >= n:
        return day * 3
    if total + a >= n:
        return day * 3 + 1
    if total + a + b >= n:
        return day * 3 + 2
    return day * 3 + 3


T = int(input())
for t in range(T):
    n, a, b, c = map(int, input().split())
    print(compute(n, a, b, c))
