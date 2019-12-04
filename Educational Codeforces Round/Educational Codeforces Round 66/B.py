# https://codeforces.com/contest/1175/problem/B
# https://codeforces.com/blog/entry/67484

# do we need to really compute the result?
# yes, since we need to return the result when there is no overflow


def solve(stack):
    res = 0
    mul = [1]
    for op, n in stack:
        if op == '+':
            res += mul[-1]
            if res > 2**32 - 1:
                return -1
        elif op == '(':
            mul.append(min(2**32, mul[-1] * n))
        else:
            mul.pop()
    return res


l = int(input())
stack = []
for _ in range(l):
    line = input()
    if line[:3] == "add":
        stack.append(("+", 1))
    elif line[:3] == 'for':
        n = int(line[4:])
        stack.append(("(", n))
    else:
        if stack[-1][0] == "(":
            stack.pop()  
        else:
            stack.append((")", 0))
res = solve(stack)

print("OVERFLOW!!!" if res == -1 else res)

# even  we pop out the "(" when continous ")", still MLE

# solution idea: 
# Thus let's push not the real multiplier to the stack but min(multiplier, 2^32)