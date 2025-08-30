# https://codeforces.com/contest/2132/problem/A

from collections import deque


def compute_result(a, b, c):

    res = deque(a)
    for i, person in enumerate(c):
        if person == 'V':
            res.appendleft(b[i])
        else:
            res.append(b[i])
    return ''.join(res)


T = int(input())

for t in range(T):
    n = int(input())
    a = input()
    m = int(input())
    b = input()
    c = input()
    print(compute_result(a, b, c))
