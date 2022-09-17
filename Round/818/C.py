# https://codeforces.com/blog/entry/106553
# https://codeforces.com/contest/1717/problem/C


def check(i, a, b, n):
    if a[i] == b[i]:
        return True
    if a[i] > b[i]:
        return False
    if b[(i + 1) % n] < b[i] - 1:
        return False
    return True


T = int(input())
for t in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # for each position i, if ai != bi, then we need ai to be increased to bi.
    # which means, we need to have aj in the right of ai that aj <= bj and bj >= bi - 1.
    for i in range(n):
        if not check(i, a, b, n):
            print('No')
            break
    else:
        print('Yes')

# Take away:
# case 0: b all equal but smaller than the max of a, should be 'No'
# case 1: b and a with the first element equals is not sufficient for 'Yes'
