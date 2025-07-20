n = int(input())

a = list(map(int, input().split()))


def solve(a):
    res = sum(a)
    if res % 2 == 1:
        return "NO"
    if max(a) > res // 2:
        return "NO"
    return "YES"


print(solve(a))
