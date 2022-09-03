n = int(input())

def solve(a, b):
    def map_(s):
        t = []
        last = ''
        cur = 0
        for c in s:
            if c == last:
                cur += 1
            else:
                t.append([c, cur]) # must be the same char
                cur = 1
                last = c
        t.append([c, cur])
        return t
  
    a = map_(a)
    b = map_(b)
    # print(a, b)
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i][0] != b[i][0]:
            return False
        if a[i][1] > b[i][1]:
            return False
    return True


for _ in range(n):
    a = input()
    b = input()
    print("YES" if solve(a, b) else "NO")