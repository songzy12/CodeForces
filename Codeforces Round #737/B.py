T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    final = {}
    for i, e in enumerate(sorted(a)):
        final[e] = i

    cut = 0
    for i in range(len(a) - 1):
        if final[a[i + 1]] - final[a[i]] != 1:
            cut += 1
    print('Yes' if cut + 1 <= k else 'No')