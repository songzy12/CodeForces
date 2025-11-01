# https://codeforces.com/contest/758/problem/D

# just dp

# no need for dp:
# for any x number, [x/10] is either
# contains less substrings (valid digits in base-n numeric system) or
# it's possible to decrease value of the last substring of number x.

n = int(input())
k = input()


def solve(k, n):
    ans = 0
    exp = 0
    cur_index = len(k)
    while cur_index != 0:
        next_index = cur_index - 1
        while next_index >= 0 and int(k[next_index:cur_index]) < n:
            if k[next_index] != '0' or next_index == cur_index - 1:
                valid_index = next_index
            next_index -= 1
        ans += int(k[valid_index:cur_index]) * n**exp
        cur_index = valid_index
        exp += 1
    return ans


print(solve(k, n))