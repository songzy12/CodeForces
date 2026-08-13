# https://codeforces.com/contest/1/problem/A


def compute_tiles(n, a):
    if n % a == 0:
        return n // a
    else:
        return n // a + 1


def solve(n, m, a):
    return compute_tiles(n, a) * compute_tiles(m, a)


if __name__ == "__main__":
    n, m, a = map(int, input().split())
    print(solve(n, m, a))
