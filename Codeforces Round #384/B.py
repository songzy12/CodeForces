n, k = map(int, raw_input().split())
len_ = [0 for i in range(n+1)]
for i in range(1, n+1):
    len_[i] = len_[i-1]*2 + 1

#print len_

def get(n, k):
    #print n, k
    if k == len_[n-1] + 1:
        return n
    if k > len_[n-1] + 1:
        return get(n - 1, k - len_[n-1] - 1)
    return get(n - 1, k)

print get(n, k)
