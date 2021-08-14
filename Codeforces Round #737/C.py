# https://codeforces.com/contest/1557/problem/C
# https://codeforces.com/contest/1557/submission/125412943

# n numbers, each has k bits. we want And >= Xor.
#
# For a single bit,
# - And = 1, Xor = 1:
#   - only n % 2 == 1
# - And = 1, Xor = 0:
#   - only n % 2 == 0
# - And = 0, Xor = 0:
#   - n % 2 == 0: 2**(n-1) - 1
#   - n % 2 == 1: 2**(n-1)
#
# dp_{i,0} is when k == i, and the most significant bit has And = 1, Xor = 0
# dp_{i,1} is when k == i, and the most significant bit has And = Xor = 1 or And = Xor = 0
# dp_i = dp_{i,0} + dp_{i,1}
#
# when n % 2 == 1, for a single bit
#   we have only 1 way to make And = 1, Xor = 1
#   we have no way to make And = 1, Xor = 0
#   we have 2**(n-1) way to make And = 0, Xor = 0
# thus
#   dp_{i,0} = 0,
#   dp_{i,1} = (1+2**(n-1)) * dp_{i-1,1}
#
# when n % 2 == 0, for a single bit
#    we have no way to make And = 1, Xor = 1
#    we have 1 way to make And = 1, Xor = 0
#    we have 2**(n-1) - 1 way to make And = 0, Xor = 0
# thus
#   dp_{i,0} = 1 * (2**(i-1))**n
#   dp_{i,1} = (2**(n-1) - 1) * (dp_{i-1,1}+dp_{i-1,0})

T = int(input())
P = 10**9 + 7

MAX_N = 4 * 10**10

pow_cache = {}


def get_pow(n, k):
    if (n, k) in pow_cache:
        return pow_cache[n, k]
    if k == 0:
        return 1
    t = get_pow(n, k // 2)
    if k % 2 == 0:
        res = (t * t) % P
    else:
        res = (t * t * n) % P
    pow_cache[n, k] = res
    return pow_cache[n, k]


def solve(n, k):
    if k == 0:
        return 1
    if n % 2 == 1:
        return get_pow(1 + get_pow(2, n - 1), k) % P
    a = 0
    b = 1
    for i in range(1, k + 1):
        b = ((get_pow(2, n - 1) - 1) * (a + b)) % P
        a = (get_pow(2, (i - 1) * n)) % P
    return (a + b) % P


for t in range(T):
    n, k = map(int, input().split())
    print(solve(n, k) % P)