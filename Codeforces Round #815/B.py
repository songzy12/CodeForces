# https://codeforces.com/contest/1720/problem/B
# https://codeforces.com/blog/entry/106136
#
# res = max1 + max2 - min1 - min2

T = int(input())
for t in range(T):
    _ = input()
    a = list(map(int, input().split()))
    a = sorted(a)
    print(a[-1]+a[-2]-a[0]-a[1])
