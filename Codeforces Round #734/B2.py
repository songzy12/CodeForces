from collections import defaultdict

T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    count = defaultdict(int)
    for element in a:
        count[element] += 1

    index_a = []
    for index, element in enumerate(a):
        index_a.append([count[element], element, index])
    index_a.sort(reverse=True)
    # print(index_a)

    colors = [0 for i in range(n)]
    i = 0
    while i < n:
        c, _, index = index_a[i]
        if c > k:
            for i_tmp in range(i, i + k):
                c_tmp, _, index_tmp = index_a[i_tmp]
                colors[index_tmp] = i_tmp - i + 1
                # print(index_tmp, i_tmp - i + 1)
            for i_tmp in range(k, c):
                c_tmp, _, index_tmp = index_a[i_tmp]
                colors[index_tmp] = 0
                # print(index_tmp, 0)
            i += c
            continue

        for i_tmp in range(i, i + (n - i) // k * k):
            c_tmp, _, index_tmp = index_a[i_tmp]
            colors[index_tmp] = (i - i_tmp) % k + 1
            # print(index_tmp, (i - i_tmp) % k + 1)
        for i_tmp in range(i + (n - i) // k * k, n):
            c_tmp, _, index_tmp = index_a[i_tmp]
            colors[index_tmp] = 0
            # print(index_tmp, 0)
        break
    print(" ".join(map(str, colors)))
