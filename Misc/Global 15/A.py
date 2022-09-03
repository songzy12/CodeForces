# https://codeforces.com/contest/1552/problem/0

T = int(input())
for t in range(T):
    n = input()
    s = input()
    sorted_s = sorted(s)

    k = 0
    for i in range(len(s)):
        if s[i] != sorted_s[i]:
            k += 1
    print(k)