# https://codeforces.com/contest/892/problem/D
#
# For a sorted array we can just cyclic shift.
# For an un-sorted array, we do the same thing:
#   replace the i-th smallest element with the (i + 1)-th smallest,
#   and replace the largest with the smallest.


def solve(n, b):
    c = [(t, i) for i, t in enumerate(b)]
    c.sort()

    d = [0 for i in range(n)]
    for i in range(n - 1):
        d[c[i + 1][-1]] = c[i][0]
    d[c[0][-1]] = c[-1][0]
    return d


if __name__ == "__main__":
    n = int(input())
    b = list(map(int, input().split()))

    print(" ".join(map(str, solve(n, b))))
