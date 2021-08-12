T = int(input())
for t in range(T):
    n = int(input())
    a = list(map(int, input().split()))

    a_max = max(a)
    a_len = len(a)
    print(a_max + (sum(a) - a_max) / (a_len - 1))
