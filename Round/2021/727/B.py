# https://codeforces.com/contest/1539/problem/B
# we can just use sum[i][j] to store the number of char [j] from s[:i+1].
# then with the question [l, r], we use just compute the number of chars sum[r][j]-sum[l][j].
# then we return \sum j*sum[r][j]-sum[l][j]

def compute_prefix_sum(s):
    # res[i] is the number of chars in s[:i]
    res = [[0 for i in range(26)] for i in range(len(s)+1)]
    for i in range(1, len(s)+1):
        res[i] = list(res[i-1])
        res[i][ord(s[i-1])-ord('a')] += 1
    return res


n, q = map(int, input().split())
s = input()

prefix_sum = compute_prefix_sum(s)
for i in range(q):
    l, r = map(int, input().split())
    res = 0
    for i in range(26):
        res += (i+1) * (prefix_sum[r][i]-prefix_sum[l-1][i])
    print(res)
