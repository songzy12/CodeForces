# http://codeforces.com/contest/1175/problem/A
# https://codeforces.com/blog/entry/67484

# n / k <= n / 2 <= n - 1
# n <= 2 * n - 2
# n >= 2

# thus, when n >= 2 and k >= 2
# we have n / k <= n - 1

t = int(input())


def solve(n, k):
    cnt = 0
    while n != 0:
        if n % k == 0:
            cnt += 1
            n //= k
        else:
            cnt += n % k
            n -= n % k
    return cnt


for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
