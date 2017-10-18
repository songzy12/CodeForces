n = int(raw_input())

def check(x):
    if x + sum(map(int, str(x))) == n:
        return True
    return False

ans = []

def get_start():
    return max(0, n - 9 * len(str(n)))

start = get_start()
for i in range(start, n + 1):
    if check(i):
        ans.append(i)

print len(ans)
for n in ans:
    print n,
print
