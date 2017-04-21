n = int(raw_input())
s = []
for t in range(n):
    s.append(raw_input())

def get_num(s, t):
    num = []
    for temp in s:
        def compute(temp):
            for i in range(len(temp)):
                if temp[i:]+temp[:i] == t:
                    return i
            return -1
        num.append(compute(temp))
    return -1 if -1 in num else sum(num)

def get_ans(s):
    ans = 1<<31-1
    for i in range(len(s[0])):
        t = s[0][i:]+s[0][:i]
        num = get_num(s, t)
        if num == -1:
            return -1
        ans = min(num, ans)
    return ans

ans = get_ans(s)
print ans
        
    
