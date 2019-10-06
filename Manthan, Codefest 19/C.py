# https://codeforces.com/contest/1208/problem/C
# https://codeforces.com/blog/entry/69357

from sys import stdin, stdout
input = stdin.readline
print = stdout.write

n = int(input())
# n % 4 == 0
res = [[0 for i in range(n)] for j in range(n)]


def group(i, j, g):
    if g == 0:
        return i, j
    elif g == 1:
        return i, j + n // 2
    elif g == 2:
        return i + n // 2, j
    elif g == 3:
        return i + n // 2, j + n // 2


for i in range(n // 2):
    for j in range(n // 2):
        base = i * (n // 2) + j 
        for g in range(4):
            x, y = group(i, j, g)
            res[x][y] = 4 * base + g

for row in res:
    print(" ".join(map(str, row)) + "\n")    