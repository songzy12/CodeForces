# https://codeforces.com/contest/2096/problem/B



def compute(l, r ,n,k):
    pairs = []
    for i in range(n):
        pairs.append([l[i], r[i]])
    pairs.sort(key = lambda x: min(x), reverse=True)

    return sum([sum(x) for x in pairs[:k-1]]) + sum([max(x) for x in pairs[k-1:]]) + 1

T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))

    print(compute(l, r, n, k))
