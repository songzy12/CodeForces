# https://codeforces.com/contest/1543/problem/D2

# the question is: what would x become if we guess y?
# for each bit, it should be (y - x + k) % k
# suppose x=y0.
# if we guess x=y1 but wrong, then the password would be set to (y1-y0) mod k.
# thus next time if we want to guess original x=y2, we should actually guess (y1-y2) mod k.
# then, if this is wrong again, the password would be set to (y1-y2)-(y1-y0) = (y0-y2) mod k.
# thus next time if we want to guess original x=y3, we should actually guess (y3-y2) mod k.
# then, password would be set to (y3-y0) mode k.
# thus we should guess (y3-y4) mod k.
# if last time we guess s, this time we want to guess t, then we should guess (t-s) mod k or (s-t) mod k.
import sys


def compute(x, y, k):
    # compute (y-x) mode k
    res = 0
    cur = 1
    while x or y:
        x0 = x % k
        y0 = y % k
        bit = (k + y0 - x0) % k
        res += bit*cur
        x = x // k
        y = y // k
        cur *= k
    return res


T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    cur = 0
    sign = 1
    for guess in range(n):
        if sign:
            guess_trans = compute(cur, guess, k)
        else:
            guess_trans = compute(guess, cur,  k)
        print(guess_trans)
        sys.stdout.flush()
        r = int(input())
        if r == 1:
            break
        cur = guess
        sign = 1 - sign
