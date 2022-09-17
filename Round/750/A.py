# https://codeforces.com/contest/1582/problem/A
t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if c % 2 == 0:
        if b % 2 == 0:
            print(a % 2)
        else:
            if a > 2:
                print(a % 2)
            else:
                print(2 - a)
    else:
        if b > 0:
            if a > 1:
                print((a - 1) % 2)
            else:
                print(1 - a)
        else:
            if a > 3:
                print((a - 3) % 2)
            else:
                print(3 - a)
