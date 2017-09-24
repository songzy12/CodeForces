n = int(raw_input())
ws = map(int, raw_input().split())
ws.sort()
#print ws
ans = 1000 * 50
for i in range(2 * n):
    for j in range(i + 1, 2 * n):
        # remove ws[i] and ws[j]
        ws_ = ws[:i] + ws[i+1:j] + ws[j+1:]
        temp = 0
        for t in range(0, 2 * n - 2, 2):
            #print t, ws_[t+1], ws_[t]
            temp += ws_[t+1] - ws_[t]
        #print ws_, i, j, temp
        ans = min(ans, temp)
print ans
