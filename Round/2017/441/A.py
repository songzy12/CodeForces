# https://codeforces.com/contest/876/problem/A


def solve(n, a, b, c):
    if n == 1:
        return 0

    return min(a, b) + (n - 2) * min([a, b, c])


if __name__ == "__main__":
    n = int(input())

    a = int(input())
    b = int(input())
    c = int(input())

    print(solve(n, a, b, c))
