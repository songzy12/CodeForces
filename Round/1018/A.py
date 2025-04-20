# https://codeforces.com/contest/2096/problem/A

def compute(n, s):
    l = 1
    r = n
    ans = []
    for c in s[::-1]:
        if c == '>':
            ans= [r] + ans
            r -=1 
        else:
            ans = [l] + ans
            l += 1
    ans = [l] + ans
    return " ".join(map(str, ans))

T = int(input())
for t in range(T):
    n = int(input())
    s = input()
    print(compute(n, s))
