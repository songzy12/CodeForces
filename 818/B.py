T = int(input())

for t in range(T):
    n, k, r, c = map(int, input().split())
    res = [['.' for i in range(n)] for j in range(n)]
    res[r - 1][c - 1] = 'X'
    for cur_r in range(n):
        cur_c = (cur_r - r + c + n) % n
        cnt = 0
        while cnt < (n // k):
            res[cur_r][cur_c] = 'X'
            cur_c = (cur_c + k) % n
            cnt += 1
    for row in res:
        print("".join(row))
