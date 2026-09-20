# https://codeforces.com/contest/892/problem/C

import math


def run_one_iteration(a):
    b = []
    for i in range(1, len(a)):
        temp = math.gcd(a[i - 1], a[i])
        if temp == 1:
            return True, []
        b.append(temp)
    return False, b


def solve(a, n):
    cnt_1 = a.count(1)  # there may be more than 1 in a
    if cnt_1 > 0:
        return n - cnt_1

    found_1, a = run_one_iteration(a)
    cnt_ops = 1
    while not found_1 and len(a) > 1:
        found_1, a = run_one_iteration(a)
        cnt_ops += 1

    if not found_1:
        return -1
    else:
        return cnt_ops + n - 1


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    print(solve(a, n))
