# https://codeforces.com/contest/765/problem/B


def check(s):
    if s and s[0] != 'a':
        return False
    cur = 'a'
    for c in s:
        if ord(c) - ord(cur) <= 0:
            continue
        if ord(c) - ord(cur) == 1:
            cur = c
            continue
        return False
    return True


if __name__ == "__main__":
    s = input()
    print('YES' if check(s) else 'NO')
