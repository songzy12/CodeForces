# https://codeforces.com/contest/892/problem/A


def solve(a, b):
    return sum(sorted(b)[-2:]) >= sum(a)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print('YES' if solve(a, b) else 'NO')
