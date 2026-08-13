# https://codeforces.com/contest/1/problem/B

from enum import Enum
import re


class Type(Enum):
    RC = 1
    Letters = 2


def get_type(s):
    if re.match(r'^R\d+C\d+$', s):
        return Type.RC
    return Type.Letters


def convert_to_RC(s):
    rc = re.split(r'(\D+)', s)
    c, r = rc[1], rc[2]
    c_ = 0
    for i in c:
        c_ = c_ * 26 + ord(i) - ord('A') + 1
    return ('R' + r + 'C' + str(c_))


def convert_to_Letters(s):
    rc = re.split(r'(\D+)', s)
    r, c = rc[2], int(rc[4])
    c_ = ''
    while c:
        # when c = 26, should print 'Z'
        res = (c - 1) % 26
        c_ = chr(res + ord('A')) + c_
        c = (c - 1 - res) // 26
    return (c_ + r)


def convert(s):
    if get_type(s) == Type.RC:
        return convert_to_Letters(s)
    return convert_to_RC(s)


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = input()
        print(convert(s))
