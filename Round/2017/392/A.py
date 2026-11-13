# https://codeforces.com/contest/758/problem/A


def solve(a):
    max_val = max(a)
    return max_val * len(a) - sum(a)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))
