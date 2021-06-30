# https://codeforces.com/contest/1539/problem/A

# NOTE: their dissatisfaction equals to the number of participants that started the contest (or starting it now), but haven't yet finished it.
# (nx - t) // x with (t//x), then t//x - 1, t//x - 2, until 1.

def compute(n, x, t):
    return t//x * max(0, n - t//x) + min(n, t//x) * (min(n, t//x)  - 1) // 2

k = int(input())
for i in range(k):
    n, x, t = map(int, input().split())
    print(compute(n, x, t))