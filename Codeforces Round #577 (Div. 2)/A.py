n, m = map(int, input().split())

s = []
for i in range(n):
    s.append(input())

res = 0
a = list(map(int, input().split()))
for i in range(m):
    temp = [t[i] for t in s]
    max_cnt = max([sum([t == c for t in temp]) for c in "ABCDE"])

    res += max_cnt * a[i]
print(res)
