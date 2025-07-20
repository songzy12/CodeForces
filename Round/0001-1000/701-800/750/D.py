# https://codeforces.com/contest/1582/problem/D

# a1 a2 + a2 (-a1) = 0
# a1 (a2 - a3) + a2 (a3 - a1) + a3 (a1 - a2) = 0

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [0 for i in range(n)]
    if n % 2 == 0:
        for i in range(n):
            b[i] = a[i // 2 * 2 + (1 - i % 2)] * (-1)**(i % 2)

    else:
        for i in range(n-3):
            b[i] = a[i // 2 * 2 + (1 - i % 2)] * (-1)**(i % 2)
        if a[-3] == a[-2] and a[-2] == a[-1]:
            b[-3] = 1
            b[-2] = 1
            b[-1] = -2
        elif a[-3] == a[-2]:
            b[-3] = a[-2] - a[-1]
            b[-2] = -a[-3]
            b[-1] = a[-3]
        elif a[-2] == a[-1]:
            b[-3] = a[-2]
            b[-2] = a[-1] - a[-3]
            b[-1] = -a[-2]
        elif a[-3] == a[-1]:
            b[-3] = a[-1] - a[-2]
            b[-2] = a[-3]
            b[-1] = -a[-3]
        else:
            b[-3] = a[-2] - a[-1]
            b[-2] = a[-1] - a[-3]
            b[-1] = a[-3] - a[-2]
    print(" ".join(map(str, b)))
