from sys import stdin,stdout
input=stdin.readline
print=stdout.write
# NOTE: python3 TLE, use pypy3, and use the above lines.

n = int(input())
dist = []
for i in range(n):
    dist.append(list(map(lambda x: 1 if x == '1' else 200, input())))
m = int(input())
p = list(map(int, input().split()))


def solve(n, dist, m, p):
    for i in range(n):
        dist[i][i] = 0
    for t in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][t]+dist[t][j])
    # print(dist)
    prev = 0
    cur = 1
    a = p[prev]
    res = [a]
    while cur < m:
        # print(prev, cur, p[prev], p[cur])
        if cur - prev == 1 and p[prev] == p[cur]:
            res.append(p[cur])
            prev = cur
            cur += 1
            continue

        b = p[cur]
        
        if dist[a-1][b-1] != cur - prev:
            res.append(p[cur - 1])
            prev = cur - 1
            cur -= 1
            a = p[prev]
        cur += 1

    res.append(p[cur - 1])
    return res


res = solve(n, dist, m, p)
print(str(len(res)) + "\n")
print(" ".join(map(str, res)))
