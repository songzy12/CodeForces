# https://codeforces.com/contest/1543/problem/D1
# password between [0, n-1], we can try n times.
# thus we can just enumerate from 0 to n-1
# suppose x=y0.
# if we guess x=y1 but wrong, then the password would be set to y0^y1
# thus next time if we want to guess original x=y2, we should actually guess y2^y1
import sys
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    cur = 0
    for guess in range(n):
        print(cur ^ guess)
        sys.stdout.flush()
        r = int(input())
        if r == 1:
            break
        # cur = cur ^ (cur ^ guess) 
        cur = guess
