n = int(raw_input())
L = map(int, raw_input().split())

L_ = [0 for i in range(n)]
for i, t in enumerate(L):
    L_[max(0, i-t)] = min(t, i)

ans = 0
cur = 0
for i, t in enumerate(L_):
    if not cur and not t:
        ans += 1
    elif not cur:
        cur = t - 1
    else:
        cur = max(cur - 1, t - 1)

print ans

