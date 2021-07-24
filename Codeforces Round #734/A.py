T = int(input())

for t in range(T):
    n = int(input())
    c = n // 3
    if n % 3 == 0:
        c1 = c2 = c
    elif n % 3 == 1:
        c1 = c + 1
        c2 = c
    else:
        c1 = c
        c2 = c + 1
    print(c1, c2)