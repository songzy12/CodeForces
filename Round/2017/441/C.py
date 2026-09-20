# https://codeforces.com/contest/876/problem/C


def check(x, n):
    if x + sum(map(int, str(x))) == n:
        return True
    return False


def get_start(n):
    return max(0, n - 9 * len(str(n)))


def solve(n):
    ans = []

    start = get_start(n)
    for i in range(start, n + 1):
        if check(i, n):
            ans.append(i)

    return ans


if __name__ == "__main__":
    n = int(input())
    ans = solve(n)
    print(len(ans))
    for x in ans:
        print(x)
