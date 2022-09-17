n = int(raw_input())
a = map(int, raw_input().split())
b = map(int, raw_input().split())
b_ = [(-num, i) for i, num in enumerate(b)]
a.sort()
b_.sort()
m = [None for i in range(n)]
for i, num in enumerate(b_):
    m[num[-1]] = a[i]
for num in m:
    print num,
