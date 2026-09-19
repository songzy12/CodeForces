# https://codeforces.com/contest/791/problem/A


def solve(x, y):
    i = 0
    while True:
        if x > y:
            return i
        else:
            i += 1
            x *= 3
            y *= 2


if __name__ == "__main__":
    x, y = map(int, input().split())
    print(solve(x, y))
