n = int(input())
a = list(map(int, input().split()))

a.sort()

met = set()
for t in a:
    if t - 1 > 0 and t - 1 not in met:
        met.add(t-1)
    elif t not in met:
        met.add(t)
    elif t + 1 not in met:
        met.add(t+1)
print(len(met))