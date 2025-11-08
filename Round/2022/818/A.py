T = int(input())
for t in range(T):
    N = int(input())
    # 3 cases, A = B, A = 2B, A = 3B
    print(N + N // 2 * 2+ N // 3 * 2)
