q = int(input())
for _ in range(q):
    n = int(input())
    p = list(map(int, input().split()))

    def solve(p, n):
        index = p.index(1)
        
        t = p[index:] + p[:index]
        for i in range(n):
            if t[i] != i+1:
                break
        else:
            return True

        t = p[index+1:] + p[:index+1]
        for i in range(n):
            if t[i] != n-i:
                break
        else:
            return True

        return False

    print("YES" if solve(p, n) else "NO")
