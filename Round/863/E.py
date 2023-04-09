# https://codeforces.com/contest/1811/problem/E


def map(n):
    ans = ''
    for i in n:
        if int(i) < 4:
            ans += i
        else:
            ans += str(int(i) + 1)
    return ans


def compute_base_9(k):
    ans = ''
    while k:
        ans = str(k % 9) + ans
        k = k // 9
    return ans


t = int(input())
for _ in range(t):
    k = int(input())
    raw_ans = compute_base_9(k)
    print(map(raw_ans))
