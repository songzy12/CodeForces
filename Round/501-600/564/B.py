n = int(input())

res = [(1, 1)]
up = True
for _ in range(n - 1):
    x, y = res[-1]
    if up:
        res.append((x, y+1))
    else:
        res.append((x+1, y))
    up = not up

size = max(res[-1])
print(size)
for x, y in res:
    print(x, y)