# https://codeforces.com/contest/1717/problem/D
# https://codeforces.com/blog/entry/106553
#
# The problem can be reformulated as follows:
#   We've got a complete binary tree with 2𝑛 leaves.
#   There's a marked edge from each intermediate node to one of its children.
#   The winner is the leaf reachable from the root via marked edges.
#   Changes modify the outgoing marked edge of a node.
#
# For each level, only one node matters: the one reachable from the root.
# 1. The winner only depends on the subset of levels we perform changes on.
# 2. Different subsets yield different winners.
#
# Then the answer is just \sum_{i=0}^{min(n,k)} \binom{n}{i}.

MOD = 10**9 + 7
MAX_F = 10**5 + 5

fact = [1 for i in range(MAX_F)]
ifact = [1 for i in range(MAX_F)]


def mult(a, b):
    return (a * b) % MOD


def power(a, n):
    if n == 0:
        return 1

    tmp = power(a, n // 2)
    if n % 2 == 0:
        return mult(tmp, tmp) % MOD
    return mult(a, mult(tmp, tmp)) % MOD


def C(n, k):
    # https://www.geeksforgeeks.org/compute-ncr-p-set-3-using-fermat-little-theorem/
    if k < 0 or k > n:
        return 0
    # print(
    #     f"fact[{n}]={fact[n]}, ifact[{n-k}]={ifact[n-k]}, ifact[{k}]={ifact[k]}"
    # )
    return mult(fact[n], mult(ifact[n - k], ifact[k]))


def init():
    n = MAX_F - 1
    for i in range(1, n + 1):
        fact[i] = mult(fact[i - 1], i)

    ifact[n] = power(fact[n], MOD - 2)
    for i in range(n - 1, 0, -1):
        ifact[i] = mult(ifact[i + 1], i + 1)


init()
n, k = map(int, input().split())
res = 0
for m in range(min(n, k) + 1):
    # print(f"n={n}, m={m}, C({n},{m})={C(n,m)}")
    res += C(n, m)
    res = res % MOD
print(res)
