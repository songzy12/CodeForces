# https://codeforces.com/contest/1720/problem/A
# https://codeforces.com/blog/entry/106136
#
# a*d*t1 = b*c*t2
# if a*d == b*c, then 0
# if a*d mod b*c == 0 or b*c mod a*d == 0, then 1
# else 2

T = int(input())
for t in range(T):
    a, b, c, d = map(int, input().split())
    if a*d == b*c:
        print(0)
    elif a*d == 0 or b*c == 0:
        print(1)
    elif ((a*d) % (b*c) == 0) or ((b*c) % (a*d) == 0):
        print(1)
    else:
        print(2)
