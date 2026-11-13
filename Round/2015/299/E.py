# https://codeforces.com/contest/535/problem/E
#
# For each index i, determine whether there exists some S, T; such that
#  S / s[i] + T / t[i] is the minimum among all s, t pairs.
#
# Convex optimization?

def solve(s, t):
    pass


if __name__ == "__main__":
    n = int(input())
    s = []
    t = []
    for i in range(n):
        si, ti = map(int, input().split())
        s.append(si)
        t.append(ti)
    print(solve(s, t))
