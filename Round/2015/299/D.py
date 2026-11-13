# https://codeforces.com/contest/535/problem/D
#
# the original s is of size n.
# the number of y's is of size m.
# given p and y
#
# if we sort y, and check each y[i] in order, we can either
# 1. find the y is invalid
# 2. find number of positions of s that can be arbitrarily assigned
#
# To find whether y is invalid quickly, something like kmp can be used.


VOCAB_SIZE = 26
MOD = 10**9 + 7


def compute_prefix_positions(p):
    """Given string p, return a list of positions i, such that p[i:] is a prefix of p.

    TODO: optimize this func.
    """
    n = len(p)
    prefixes = set()
    for i in range(n):
        if p[i:] == p[:n-i]:
            prefixes.add(i)
    return prefixes


def is_valid(index, prefix_positions):
    """Check if p[index:] can be a valid prefix of p."""
    return index in prefix_positions


def power_mod(base, exponent, mod):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent //= 2
    return result


def solve(n, p, y):
    prefix_positions = compute_prefix_positions(p)
    # print("prefix_positions:", prefix_positions)

    arbitrary_positions = 0
    y.sort()
    last_y = None
    for yi in y:
        # print("yi:", yi, "last_y:", last_y)
        if last_y is None:
            arbitrary_positions += yi - 1
        elif yi - last_y >= len(p):
            arbitrary_positions += yi - last_y - len(p)
        else:
            if not is_valid(yi - last_y, prefix_positions):
                return 0
        last_y = yi
    arbitrary_positions += (n + 1) - last_y - len(p)

    # print("arbitrary_positions:", arbitrary_positions)

    return power_mod(VOCAB_SIZE, arbitrary_positions, MOD)


if __name__ == "__main__":
    n, m = map(int, input().split())
    p = input()
    y = list(map(int, input().split()))
    print(solve(n, p, y))
