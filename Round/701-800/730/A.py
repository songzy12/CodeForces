# https://codeforces.com/contest/1543/problem/A
# (a, b) = (b, a-b)

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    # now a >= b
    if a == b:
        print(0, 0)
        continue
    target = a - b
    b_res = b % target
    print(target, min(target - b_res, b_res))
