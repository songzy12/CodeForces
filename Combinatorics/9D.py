# https://codeforces.com/problemset/problem/9/D
#
# Compute the number of binary search trees that has n nodes and height not lower than h.
#   where n \le 35, h \le n
#
# Thoughts:
#   let dp(n, h) denodes the number of binary search trees that have n nodes and heights not lower than h;
#   let f(n) denotes the number of any binary search trees that have n nodes. Then we have
#   dp(n, h) = \sum_{i=0}^{n-1}[dp(i, h-1) * f(n-i-1) + dp(n-i-1, h-1) * f(i) - dp(i, h-1) * dp(n-i-1, h-1)]
#     if h > n, dp(n, h) == 0; 
#     if n <= 1, dp(n, h) = 1; 
#   f(n) = \sum_{i=0}^{n-1}[f(i) * f(n-1-i)]
#      if n == 0, f(n) = 1

f = {}
dp = {}


def get_f(n):
    if n in f:
        return f[n]
    if n == 0:
        return 1
    res = 0
    for i in range(0, n):
        res += get_f(i) * get_f(n - 1 - i)
    f[n] = res
    return res


def get_dp(n, h):
    if (n, h) in dp:
        return dp[n, h]
    if h > n:
        return 0
    if n <= 1:
        return 1
    res = 0
    for i in range(0, n):
        res += get_dp(i, h - 1) * get_f(n - i - 1) + \
            get_dp(n - i - 1, h - 1) * get_f(i) - \
            get_dp(i, h - 1) * get_dp(n - i - 1, h - 1)
    dp[n, h] = res
    return res


n, h = map(int, input().split())
print(get_dp(n, h))
