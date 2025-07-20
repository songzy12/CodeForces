# https://codeforces.com/contest/1811/problem/0


def compute(s, d):
    for i in range(len(s)):
        if d > s[i]:
            return s[:i] + d + s[i:]
    return s + d


t = int(input())
for _ in range(t):
    n, d = input().split()
    s = input()
    print(compute(s, d))
