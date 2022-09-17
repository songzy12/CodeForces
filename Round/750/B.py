# https://codeforces.com/contest/1582/problem/B
# count n_0, n_1, answer is n_1 * 2**n_0

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    n0 = a.count(0)
    n1 = a.count(1)
    print(n1 * 2**n0)
