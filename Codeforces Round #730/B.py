# https://codeforces.com/contest/1543/problem/B
# distribute as even as posisble

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    x = sum_a % n
    print(x*(n-x))
