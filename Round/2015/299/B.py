# https://codeforces.com/contest/535/problem/B


def count(n, index, length):
    if index == length - 1:
        return 1 if n[index] == '4' else 2
    return (2**(length-index-1) if n[index] == '4' else 2**(length-index)) + \
           count(n, index+1, length)


def solve(n):
    # We can count the number of lucky numbers <= n recursively
    # 1. If the first digit is '4', then its index is
    #   a. the count of all lucky numbers with fewer digits
    #   b. the count of lucky numbers <= the rest.
    # 2. If the first digit is '7', then its index is
    #   a. the count of all lucky numbers with the same digits starting with '4'
    #      i. which equals to the count of all lucky numbers with fewer digits
    #   b. the count of all lucky numbers with fewer digits
    #   c. the count of lucky numbers <= the rest.
    return count(n, 0, len(n))


if __name__ == "__main__":
    n = input()
    print(solve(n))
