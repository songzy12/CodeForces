# https://codeforces.com/contest/876/problem/B

from collections import Counter


def find_mod_with_max_count(nums, m):
    mods = list(map(lambda x: x % m, nums))
    return Counter(mods).most_common()[0]


def solve(nums, k, m):
    mod, max_count = find_mod_with_max_count(nums, m)

    if max_count < k:
        return 'No', None

    ans = list(filter(lambda x: x % m == mod, nums))
    return 'Yes', ans[:k]


if __name__ == "__main__":
    n, k, m = map(int, input().split())
    nums = list(map(int, input().split()))

    status, ans = solve(nums, k, m)
    if status == 'No':
        print('No')
    else:
        print('Yes')
        print(' '.join(map(str, ans)))
