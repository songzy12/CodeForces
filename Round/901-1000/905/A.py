# https://codeforces.com/contest/1883/problem/A

def compute_steps_between(a, b):
    if b != 0 and a != 0:
        return abs(a - b)
    if a == 0 and b == 0:
        return 0
    return 10 - (a + b)


def compute_steps(digits):
    # print(digits)
    digits = [1] + digits
    res = 0
    for i in range(len(digits) - 1):
        res += compute_steps_between(digits[i], digits[i+1])
        res += 1
    return res


t = int(input())
for _ in range(t):
    digitis = list(map(int, list(input())))
    print(compute_steps(digitis))
