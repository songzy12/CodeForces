# https://codeforces.com/contest/1811/problem/D

MAX_N = 45
F = [1, 1]
for _ in range(MAX_N - 1):
    F.append(F[-1] + F[-2])


def isValid(n, x, y):
    if n == 1:
        return True

    if y > F[n]:
        next_x = y - F[n]
    elif y <= F[n + 1] - F[n]:
        next_x = y
    else:
        return False
    return isValid(n - 1, next_x, x)


t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    print("Yes" if isValid(n, x, y) else "No")
