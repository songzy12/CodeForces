# https://codeforces.com/contest/765/problem/C


def solve(a, b, k):
    win_a = a // k
    win_b = b // k

    left_a = a % k
    left_b = b % k
    if left_a > win_b * (k - 1):
        return -1
    if left_b > win_a * (k - 1):
        return -1

    return win_a + win_b


if __name__ == "__main__":
    k, a, b = map(int, input().split())
    print(solve(a, b, k))
