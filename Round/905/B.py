# https://codeforces.com/contest/1883/problem/B

def compute_num_odd(s):
    num_odd = 0
    for c in set(s):
        num_odd += s.count(c) % 2 == 1
    return num_odd

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    num_odd = compute_num_odd(s)
    print("YES" if num_odd - 1 <= k else "NO")

