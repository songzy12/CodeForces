# https://codeforces.com/contest/862/problem/D

from sys import stdout


def get_hamming_distance(s):
    print("?", s)
    stdout.flush()
    return int(input())


def compute(length, num0, num1):
    return (length+num1-num0)/2, (length-num1+num0)/2


def binary_search(l, r, target, a):
    # [l ,r] contain target
    while l < r:
        m = (l + r) // 2
        b = get_hamming_distance(
            '0' * (l - 1) + '1' * (m - l + 1) + '0' * (n - m))
        cnt = compute(m - l + 1, a, b)

        if cnt[target]:
            r = m
        else:
            l = m + 1
    return l


def solve(n):
    a = get_hamming_distance('0' * n)
    b = get_hamming_distance('0' * (n-1) + '1')
    cnt = compute(1, a, b)

    if cnt[0]:
        # find pos of 1
        r = binary_search(1, n - 1, 1, a)
        return n, r
    else:
        # find pos of 0
        l = binary_search(1, n - 1, 0, a)
        return l, n


if __name__ == "__main__":
    n = int(input())
    l0, l1 = solve(n)
    print('!', l0, l1)
    stdout.flush()
